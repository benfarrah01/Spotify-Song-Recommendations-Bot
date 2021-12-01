import os
import random
import json
import spotify.sync as spotify

def load_file(filename):
    fh = open(filename, "r")
    data = json.load(fh)
    return data

def pick_one(data):
    return random.choice(data)

def main():
    genre = loadfile("data/genre.txt")
    
    genre = genre["genre"]
    
    genre = pick_one(genre)

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('{genre}', types=['playlist'],limit=50)


for playlist in result.playlists:
    tracks = playlist.get_all_tracks()
    track = random.choice(tracks)
    print(track.popularity)
    print(f"This weekend, listen to {track.name} by {track.artist.name}. It's good.")
    
client.close()