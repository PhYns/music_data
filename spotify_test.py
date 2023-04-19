from services_sessions.spotify_service import spotify_session

# Test Spotify
CalvinHarris_uri = '7CajNmpbOovFoOoasH2HaY'
Months_uri = 'spotify:album:7CajNmpbOovFoOoasH2HaY'
response = spotify_session.artist_albums(artist_id=CalvinHarris_uri)
albums = response['items']
while response['next']:
    response = spotify_session.next(response)
    albums.extend(response['items'])
for album in albums:
    print(album['name'])
