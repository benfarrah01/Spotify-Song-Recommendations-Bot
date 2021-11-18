# This is the Rock Playlist File 
# This will get the a random song from the Rock This playlist in Spotify

import os
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('Rock This', types=['playlist'])

# for playlist in result.playlists:
#     print(playlist)

tracks = get_all_tracks()
print(tracks)
    
client.close()