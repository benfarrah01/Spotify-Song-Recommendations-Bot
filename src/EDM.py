import os
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('mint', types=['playlist'])

for playlist in result.playlists:
    print(playlist)

client.close()

# This is the EDM Playlist File 
# This will get the a random song from the mint playlist in Spotify