import spotipy  
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth  
from objects import Song
  
sp_oauth = SpotifyOAuth(client_id='47d9de416fa14f4aa93dea3de9ef211c', client_secret='48c9ba4eebc3415ea9f50526cc64828c', redirect_uri='http://localhost:3000', scope=None)  
  
access_token = sp_oauth.get_cached_token()  

sp = Spotify(auth_manager=sp_oauth)  

sp.user_playlist_tracks

def get_all_playlists_titles(username):
    results = sp.user_playlists(username)

    playlists = {}
    for playlist in results['items']:
        playlists[playlist['name']] = playlist['id']
    return playlists


def get_playlist_tracks(playlist_id):
    contents = []
    results = sp.playlist_tracks(playlist_id, fields='items.track.name, items.track.id, items.track.uri, items.track.explicit, items.track.artists, items.track.album.name, items.track.popularity, total', limit=100, offset=0, market=None, additional_types=('track', 'episode',))
    tracks = results['items']
    for track in tracks:
        album = track['track']['album']['name']
        title = track['track']['name']
        id = track['track']['id']
        uri = track['track']['uri']
        explicit = track['track']['explicit']
        popularity = track['track']['popularity']
        if len(track['track']['artists']) == 1:
            artists = track['track']['artists'][0]['name']
        else:
            contributors = []
            for a in track['track']['artists']:
                contributors.append(a['name'])
            s = ", "
            artists = s.join(contributors)

        s = Song(name=title, id=id, artists=artists, album=album, uri=uri, explicit=explicit, popularity=popularity)
        contents.append(s)
        # print(f"Song: {title}") 
        # print(f"By: {artists}") 
        # print(f"Album: {album}")
        # print()
    if len(contents) == 100:
        contents.append("Showing the first 100 tracks of the playlist. You can view the entire playlist in the Spotify App")
    return contents


pls = get_all_playlists_titles('thelogicalpianist')
print(pls)

songs = get_playlist_tracks(pls["Worship"])

for s in songs:
    print(s)