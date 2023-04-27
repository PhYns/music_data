from services_sessions.spotify_service import SpotifySession
spotify = SpotifySession()

# Test Spotify Session
CalvinHarris_uri = '7CajNmpbOovFoOoasH2HaY'
Months_uri = 'spotify:album:7CajNmpbOovFoOoasH2HaY'
response = spotify.get_session().artist_albums(artist_id=CalvinHarris_uri)
albums = response['items']
while response['next']:
    response = spotify.get_session().next(response)
    albums.extend(response['items'])
for album in albums:
    print(album['name'])
