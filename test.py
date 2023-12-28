import spotipy  
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth  
  
sp_oauth = SpotifyOAuth(client_id='client_id', client_secret='client_secret', redirect_uri='http://localhost:3000', scope=None)  
  
access_token = sp_oauth.get_cached_token()  

sp = Spotify(auth_manager=sp_oauth)  

results = sp.user_playlists('thelogicalpianist')

for playlist in results['items']:
    print(playlist['name'])