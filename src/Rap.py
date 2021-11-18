# This is the Rap Playlist File 
# This will get the a random song from the RapCaviar playlist in Spotify
import os
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('RapCaviar', types=['playlist'])

for playlist in result.playlists:
    print(playlist)

client.close()