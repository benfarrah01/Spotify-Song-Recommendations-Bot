import os
import random
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('country', types=['playlist'],limit=10)

songs = {}
for playlist in result.playlists:
    tracks = playlist.get_all_tracks()
    track = random.choice(tracks)
    songs[f'{track.name}'] = track.popularity
print(songs)
print(max(songs, key=songs.get))
client.close()
