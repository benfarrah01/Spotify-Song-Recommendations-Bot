# This is the Playlist File 
# This is a class for playlists

import os
import random
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

class PlaylistSearch:
    
    def __init__(self): #essential information class needs
        self.playlist = "PlaylistSearch"

    def get_playlist(self):
        client = spotify.Client(CLIENT, SECRET)
        result = client.search(playlist, types=['playlist'])
        result = random.choice(result)
        return result

    def get_tracks(self, result):
        for playlist in result.playlists:
            tracks = playlist.get_all_tracks()
            track = random.choice(tracks)
        return f"My mixtape has the song {track.name} by {track.artist.name}. Hell yeah."
        client.close()
        
class GenreSearch:
    
    def __init__(self): #essential information class needs
        self.genre = "GenreSearch"

    def get_genre(self):
        client = spotify.Client(CLIENT, SECRET)
        result = client.search(genre_name, types=['genre'])
        return result