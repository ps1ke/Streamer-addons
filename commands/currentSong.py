import sys
sys.path.append("..")
from lib import spotify
import json
import urllib
from bs4 import BeautifulSoup
import time


print "getting keys \n"
oauth = spotify.get_oauth_token()
csrf = spotify.get_csrf_token()

print "Ready!! GLHF"

nameSong = ""
nameArtist = ""
nameAlbum = ""
trackURL = ""

while True:

    response = spotify.get_status(oauth, csrf)
    
    currentSong = response.get("track").get("track_resource").get("name")
    
    if nameSong != currentSong:
        nameSong = currentSong
        
        nameArtist = response.get("track").get("artist_resource").get("name")
        nameAlbum = response.get("track").get("album_resource").get("name")

        trackURL = response.get("track").get("track_resource").get("location").get("og")
        soup = BeautifulSoup(urllib.urlopen(trackURL).read(), "html.parser")
        imageUrl = soup.find_all("div", "mo-image")[1]["data-bg2x"].replace("\\", "/")

        output = open("output/currentSong.txt", "w+")
        output.write(nameArtist + " || " + currentSong + "\n")
        output.write(nameAlbum)
        output.close()

        urllib.urlretrieve("http:" + imageUrl, "output/albumArtwork.jpg") 

    time.sleep(5)
