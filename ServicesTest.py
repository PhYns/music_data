import Sessions.Spotify as Spotify

# Test Spotify
CalvinHarris_uri = '7CajNmpbOovFoOoasH2HaY'
Months_uri = 'spotify:album:7CajNmpbOovFoOoasH2HaY'
results = Spotify.SpotifySession.artist_albums(artist_id=CalvinHarris_uri)
albums = results['items']
while results['next']:
    results = SpotifySession.next(results)
    albums.extend(results['items'])
for album in albums:
    print(album['name'])