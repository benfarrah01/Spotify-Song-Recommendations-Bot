class Song:

    def __init__(self, track):
        self.artist = track.artist.name
        self.title = track.name
        self.popularity = track.popularity

    def song_as_dict(self):
        return {
            "artist": self.artist,
            "title" : self.title,
            "popularity": self.popularity
        }

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.popularity})"
