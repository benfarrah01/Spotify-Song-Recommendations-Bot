import os
import random
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('', types=['playlist'],limit=10)


for playlist in result.playlists:
    tracks = playlist.get_all_tracks()
    track = random.choice(tracks)
    print(track.popularity)
    print(f"This weekend, listen to {track.name} by {track.artist.name}. It's good.")
    
client.close()