from spotipy import oauth2, Spotify
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from services_sessions.credentials import spotify_credentials as credential

# Create Spotify Session
client_credentials = oauth2.SpotifyClientCredentials(client_id=credential.ClientId, client_secret=credential.ClientSecret)
spotify_session = Spotify(client_credentials_manager=client_credentials)
