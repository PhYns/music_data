import spotipy
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Credentials import SpotifyCredentials as Credential

# Create Spotify Session
ClientCredentials = spotipy.oauth2.SpotifyClientCredentials(client_id=Credential.ClientId, client_secret=Credential.ClientSecret)
SpotifySession = spotipy.Spotify(client_credentials_manager=ClientCredentials)
