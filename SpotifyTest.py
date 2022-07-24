from ServicesSessions import SpotifyService

# Test Spotify
CalvinHarris_uri = '7CajNmpbOovFoOoasH2HaY'
Months_uri = 'spotify:album:7CajNmpbOovFoOoasH2HaY'
results = SpotifyService.SpotifySession.artist_albums(artist_id=CalvinHarris_uri)
albums = results['items']
while results['next']:
    results = SpotifyService.SpotifySession.next(results)
    albums.extend(results['items'])
for album in albums:
    print(album['name'])
