class GenreSearch:
    CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
    SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')
    
    def __init__(self): #essential information class needs
        self.genre = "GenreSearch"

    def get_genre(self):
        client = spotify.Client(CLIENT, SECRET)
        result = client.search(genre_name, types=['genre'])
        return result