from spotipy import oauth2, Spotify
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from services_sessions.credentials import spotify_credentials as credential

# Create Spotify Session
scope = ["user-library-read", "user-read-currently-playing", "playlist-modify-private", "user-follow-modify",
         "user-library-modify", "playlist-read-private"]
spotify_session = Spotify(auth_manager=oauth2.SpotifyOAuth(client_id=credential.ClientId,
                                                           client_secret=credential.ClientSecret,
                                                           redirect_uri="https://localhost/",
                                                           scope=scope))
