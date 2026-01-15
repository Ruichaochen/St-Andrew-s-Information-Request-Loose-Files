import sqlite3
import os
import json
import requests
import auth_handler

def get_all_artists_from_tracks(tracks):
    if not os.path.isfile("track_data.json"):
        with open("track_data.json","w") as f:
            f.write("{}")
    if not os.path.isfile("albums.json"):
        with open("albums.json","w") as f:
            f.write("{}")        
    track_data = json.load(open("track_data.json", encoding="utf8"))
    albums = json.load(open("albums.json", encoding="utf8"))
    to_get = []
    for track in tracks:
        if not (track in track_data):
            to_get.append(track)
    for i in range(0, len(to_get),50):
        tracks_list = ",".join(uri.split(":")[2] for uri in tracks[i:i+50])
        headers = {"Authorization" : "Bearer " + auth_handler.get_token()}
        artists_request = requests.get("https://api.spotify.com/v1/tracks?ids="+tracks_list, headers = headers)
        track_artists_data = artists_request.json()
        print(artists_request)
        for track in track_artists_data["tracks"]:
            track_data[track["uri"]] = {"artists": '["' + "','".join([artist["uri"] for artist in track["artists"]]) + '"]', "album_uri": track["album"]["uri"]}
            if not (track["album"]["uri"] in albums):
                albums[track["album"]["uri"]] = {"name": track["album"]["name"], "images": track["album"]["images"]}
    json.dump(track_data, open("track_data.json", "w"))
    json.dump(albums, open("albums.json", "w"))
    return track_data

def get_unique_tracks():
    tracks = set()
    files = [file for file in os.listdir("Spotify Extended Streaming History") if file.endswith(".json") and file.startswith("Streaming_History_Audio_")]
    for file in files:
        listening_data = json.load(open("Spotify Extended Streaming History/"+file, encoding="utf8"))
        for i in listening_data:
            if i["spotify_track_uri"] != None:
                tracks.add(i["spotify_track_uri"])
    tracks = list(tracks)
    return tracks


def import_listening_data():
    tracks = get_unique_tracks()
    track_data = get_all_artists_from_tracks(tracks)
    with sqlite3.connect('listening_data.db') as user_data:
        cursor = user_data.cursor()
        files = [file for file in os.listdir("Spotify Extended Streaming History") if file.endswith(".json") and file.startswith("Streaming_History_Audio_")]
        for file in files:
            listening_data = json.load(open("Spotify Extended Streaming History/"+file, encoding="utf8"))
            for item in listening_data:
                if item["ms_played"] >= 30000 and item["spotify_track_uri"] != None:
                    listens = cursor.execute("INSERT INTO LISTENING_DATA VALUES(?, ?, ?, ?, ?, ?)", (item["ts"], item["ms_played"], item["master_metadata_track_name"], track_data[item["spotify_track_uri"]]["artists"], item["master_metadata_album_album_name"],track_data[item["spotify_track_uri"]]["album_uri"]))

def create_database():
    with sqlite3.connect('listening_data.db') as user_data:
        cursor = user_data.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS LISTENING_DATA (
                        timestamp TIMESTAMP UNIQUE NOT NULL,
                        time_played INTEGER NOT NULL,
                        track_name TEXT,
                        track_artists TEXT,
                        album_name TEXT,
                        album_uri TEXT
                    )""")
create_database()
#import_listening_data()
with sqlite3.connect('listening_data.db') as user_data:
    cursor = user_data.cursor()
    print(sum([dur[0] for dur in cursor.execute("SELECT time_played FROM LISTENING_DATA, json_each(track_artists) WHERE LOWER(json_each.value) = LOWER('spotify:artist:2hR4h1Cao2ueuI7Cx9c7V8') AND timestamp >= '2025-01-01';").fetchall()]))
    print(sum([dur[0] for dur in cursor.execute("SELECT time_played FROM LISTENING_DATA as song, json_each(song.track_artists) WHERE LOWER(json_each.value) = LOWER('spotify:artist:2hR4h1Cao2ueuI7Cx9c7V8')").fetchall()]))
