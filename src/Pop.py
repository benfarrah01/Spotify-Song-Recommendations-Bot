import os
import random
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('Today/s Top Hits', types=['playlist'])

for playlist in result.playlists:
    tracks = playlist.get_all_tracks()
    track = random.choice(tracks)
    print(f"We recommend {track.name} by {track.artist.name} to listen to!")

client.close()

