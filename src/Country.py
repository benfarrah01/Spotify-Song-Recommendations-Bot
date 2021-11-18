import os
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('Hot Country', types=['playlist'])

for playlist in result.playlists:
    print(playlist)

client.close()

# This is the Country Playlist File 
# This will get the a random song from the Hot Country playlist in Spotify