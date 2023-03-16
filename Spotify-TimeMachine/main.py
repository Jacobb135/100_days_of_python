from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


date = input("What day would you like to travel to? Must be in this format YYYY-MM-DD: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}/"
CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = "http://example.com"


response = requests.get(billboard_url)
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")
titles = soup.select(selector="li ul li h3")
title_list = [title.text.strip() for title in titles]
print(title_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user = sp.me()["display_name"]


year = date.split("-")[0]
print(year)
song_uris = []
for title in title_list:
    result = sp.search(q=f"track: {title}, year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        print(f"{title} doesn't exist in Spotify: Skipped")
print(song_uris)

my_playlist = sp.user_playlist_create(user=f"{user}", name=f"{year} TOP 100", public=False,
                                      description="A BLAST FROM THE PAST PERHAPS?")
playlist_id = my_playlist["id"]
sp.playlist_add_items(playlist_id, song_uris)
