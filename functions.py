import spotipy  
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth  
  
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
    results = sp.playlist_tracks(playlist_id, fields='items.track.name, items.track.id, items.track.artists, items.track.album.name, total', limit=100, offset=0, market=None, additional_types=('track', 'episode',))
    tracks = results['items']
    for track in tracks:
        album = track['track']['album']['name']
        title = track['track']['name']
        if len(track['track']['artists']) == 1:
            artists = track['track']['artists'][0]['name']
        else:
            contributors = []
            for a in track['track']['artists']:
                contributors.append(a['name'])
            s = ", "
            artists = s.join(contributors)
        print(f"Song: {title}") 
        print(f"By: {artists}") 
        print(f"Album: {album}")
        print()


pls = get_all_playlists_titles('thelogicalpianist')

get_playlist_tracks(pls["Stompin' and Hollerin'"])