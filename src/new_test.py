from Search import PlaylistSearch
from Search import GenreSearch

def main():
    music = PlaylistSearch()
    obj = music.get_playlist()
    print(obj)
    
main()