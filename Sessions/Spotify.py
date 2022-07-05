import spotipy
import os

# Create Spotify Session
client_id = os.environ['CLIENT_ID_GITSECRET']
client_secret = os.environ['CLIENT_SECRET_GITSECRET']
SpotifyCredentials = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
SpotifySession = spotipy.Spotify(client_credentials_manager=SpotifyCredentials)

# Testing
CalvinHarris_uri = spotipy.Spotify.artist(artist_id='7CajNmpbOovFoOoasH2HaY')
Months_uri = spotipy.Spotify.album(album_id='spotify:album:7CajNmpbOovFoOoasH2HaY')
results = spotipy.Spotify.artist_albums(Months_uri, CalvinHarris_uri)
albums = results['items']
while results['next']:
    results = SpotifySession.next(results)
    albums.extend(results['items'])
for album in albums:
    print(album['name'])
