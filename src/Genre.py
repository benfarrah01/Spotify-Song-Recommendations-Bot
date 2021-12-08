import os
import random
import json
import spotify.sync as spotify
from Song import Song


def load_file(filename):
    fh = open(filename, "r")
    data = json.load(fh)
    return data

def pick_one(data):
    return random.choice(data)

def most_popular(songs):
    return max(songs, key=lambda x:x['popularity'])

def get_song():
    genre = load_file("data/genres.json")
    genre = genre["genres"]
    genre = pick_one(genre)
    #print(genre)

    CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
    SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

    client = spotify.Client(CLIENT, SECRET)
    result = client.search(genre, types=['playlist'],limit=5)

    songs = []
    for playlist in result.playlists:
        tracks = playlist.get_all_tracks()
        track = random.choice(tracks)
        songs.append(Song(track).song_as_dict())
    song = most_popular(songs)
    client.close()
    return song


    
