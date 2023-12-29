import spotipy  
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth  

class Artist():
    def __init__(self, name, id, followers, genre, popularity, uri):
        super().__init__()
        self.name = name
        self.id = id
        self.followers = followers
        self.genre = genre
        self.popularity = popularity
        self.uri = uri


class Song():
    def __init__(self, name, id, artists, album, uri, explicit):
        super().__init__()
        self.name = name
        self.id = id
        self.artists = artists
        self.album = album
        self.uri = uri
        self.explicit = explicit

    
