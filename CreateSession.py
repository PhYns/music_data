import spotipy, tidalapi, Credentials

CalvinHarris_uri = '7CajNmpbOovFoOoasH2HaY'
Months_uri = 'spotify:album:7CajNmpbOovFoOoasH2HaY'

# Create Spotify Session
Spotify = spotipy.Spotify(client_credentials_manager=Credentials.SpotifyCredentials)
results = spotipy.Spotify.artist_albums(Months_uri,CalvinHarris_uri)
albums = results['items']
while results['next']:
    results = Spotify.next(results)
    albums.extend(results['items'])
for album in albums:
    print(album['name'])

# Create Tidal Session
session = tidalapi.Session()
session.login_oauth_simple()
tracks = session.get_album_tracks(album_id=16909093)
for track in tracks:
    print(track.name)