import pandas as pd
import os
import requests
from mutagen.ogg import OggFileType
from mutagen.oggvorbis import OggVorbis
from mutagen.flac import Picture
import base64
import threading
def tag(file,image,title,album,artist):
    path = os.path.join(r'C:\Users\R\Desktop\oggify_csv-main\target\debug\my_playlistcave',file)
    audio = OggVorbis(path)
    image = os.path.join(r'C:\Users\R\Desktop\oggify_csv-main\target\debug\album_covers',image)
    with open(image, "rb") as h:
        data = h.read()

    picture = Picture()
    picture.data = data
    picture.type = 17
    picture.desc = u"Cover"
    picture.mime = u"image/jpeg"
    picture.width = 100
    picture.height = 100
    picture.depth = 24

    picture_data = picture.write()
    encoded_data = base64.b64encode(picture_data)
    vcomment_value = encoded_data.decode("ascii")

    audio["metadata_block_picture"] = [vcomment_value]
    audio["title"] = title
    audio["album"] = album
    audio["artist"] = artist
    audio.save()
def twice(file,image,title,album,artist):
    for i in range(0,2):
        tag(file,image,title,album,artist)

df = pd.read_csv('my_playlistcave.csv')
songs = os.listdir("C:\\Users\\R\\Desktop\\oggify_csv-main\\target\\debug\\my_playlistcave")
for i,name in enumerate(df["Track Name"]):
    try:
        open("album_covers/"+df[df["Track Name"] == name]["Album Image URL"][i].split("/")[len(df[df["Track Name"] == name]["Album Image URL"][i].split("/"))-1]+".jpg", 'r')
    except FileNotFoundError:
        img_data = requests.get(df[df["Track Name"] == name]["Album Image URL"][i]).content
        handler = open("album_covers/"+df[df["Track Name"] == name]["Album Image URL"][i].split("/")[len(df[df["Track Name"] == name]["Album Image URL"][i].split("/"))-1]+".jpg", 'wb')
        handler.write(img_data)
    for index,v in enumerate(songs):
        if name.replace(" ","_").replace(",_",",").replace("/","") in v.split("-")[len(v.split("-"))-1]:
            print("Found",v)
            imagename = df[df["Track Name"] == name]["Album Image URL"][i].split("/")[len(df[df["Track Name"] == name]["Album Image URL"][i].split("/"))-1]+".jpg"
            threading.Thread(target=twice, args=(v,imagename,name,df[df["Track Name"] == name]["Album Name"][i],df[df["Track Name"] == name]["Album Artist Name(s)"][i])).start()
            songs.pop(index)
print(songs)
