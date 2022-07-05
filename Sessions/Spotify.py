import spotipy
import Credentials.SpotifyCredentials as Credential

# Create Spotify Session
ClientCredentials = spotipy.oauth2.SpotifyClientCredentials(client_id=SpotifyCredentials.ClientId, client_secret=SpotifyCredentials.ClientSecret)
SpotifySession = spotipy.Spotify(client_credentials_manager=ClientCredentials)
