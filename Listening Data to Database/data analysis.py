import requests   
from auth_handler import get_token
import datetime
import urllib
import json
import time

##def get_played_after():
##    month = datetime.datetime(2025, datetime.datetime.now().month-1, 1, 0, 0, tzinfo = datetime.timezone.utc)
##    headers = {'Authorization': 'Bearer ' + get_token()}
##    body = {"limit" : 50} #{"after" : month_epoch, "limit" : 50}
##    done = False
##    api_endpoint = "https://api.spotify.com/v1/me/player/recently-played?" + urllib.parse.urlencode(body)
##    tracks_played_count = {}
##    while not done and api_endpoint is not None:
##        print("made request")
##        month_data = requests.get(api_endpoint, headers=headers)
##        month_data_json = month_data.json()
##        print(month_data_json["cursors"])
##        api_endpoint = "https://api.spotify.com/v1/me/player/recently-played?" + urllib.parse.urlencode({"limit" : 50, "before" : month_data_json["cursors"]["before"]})
##        for track in month_data_json["items"][::-1]:
##            played_at = datetime.datetime.fromisoformat(track["played_at"])
##            if played_at < month:
##                print(played_at)
##                done = True
##                break
##            else:
##                track_name = track["track"]["name"]
##                if track_name not in tracks_played_count:
##                    tracks_played_count[track_name] = 1
##                else:
##                    tracks_played_count[track_name] += 1
##        time.sleep(5)
##    return tracks_played_count


##def get_played_after():
##    current_month = datetime.datetime(2025, datetime.datetime.now().month-1, 1, 0, 0, tzinfo = datetime.timezone.utc).timestamp()
##    month_epoch = int(datetime.datetime(2025, datetime.datetime.now().month-6, 1, 0, 0, tzinfo = datetime.timezone.utc).timestamp())*1000
##    print(month_epoch)
##    headers = {'Authorization': 'Bearer ' + get_token()}
##    body = {"after" : month_epoch, "limit" : 50}
##    done = False
##    api_endpoint = "https://api.spotify.com/v1/me/player/recently-played?" + urllib.parse.urlencode(body)
##    tracks_played_count = {}
##    while not done and api_endpoint is not None:
##        print("requested page:", api_endpoint)
##        month_data = requests.get(api_endpoint, headers=headers)
##        month_data_json = month_data.json()
##        api_endpoint = month_data_json["next"]
##        for track in month_data_json["items"][::-1]:
##            track_name = track["track"]["name"]
##            if track_name not in tracks_played_count:
##                tracks_played_count[track_name] = 1
##            else:
##                tracks_played_count[track_name] += 1
##    return tracks_played_count

def get_user_top(item_type, length="short_term"):
    headers = {'Authorization': 'Bearer ' + get_token()}
    body = {"time_range" : length, "limit" : 5}
    top = requests.get(f"https://api.spotify.com/v1/me/top/{item_type}?" + urllib.parse.urlencode(body), headers=headers).json()
    return [item["name"] for item in top["items"]]
  
    
top_tracks = get_user_top("tracks", "long_term")
top_artists = get_user_top("artists", "long_term")

print(top_tracks)
print(top_artists)
