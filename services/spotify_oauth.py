import spotipy
from spotipy.oauth2 import SpotifyOAuth

#le tue credenziali le trovi nella dashboard di prima
SPOTIFY_CLIENT_ID = "774e83e62c3d47aaa319fada2ea26fcc"
SPOTIFY_CLIENT_SECRET = "6599f2ff0d994565a1975ba8fde8aca0"
SPOTIFY_REDIRECT_URI = "https://ubiquitous-spoon-74476v4pgrp3x6qv-5000.app.github.dev/callback" #dopo il login andiamo qui

#config SpotifyOAuth per l'autenticazione e redirect uri
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private", #permessi x informazioni dell'utente
    show_dialog=True #forziamo la richiesta di inserire new credenziali
)

def get_spotify_object (token_info):
    return spotipy.Spotify(auth=token_info['access_token'])