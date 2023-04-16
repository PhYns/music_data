from ServicesSessions import spotify_service

# Test Spotify
CalvinHarris_uri = '7CajNmpbOovFoOoasH2HaY'
Months_uri = 'spotify:album:7CajNmpbOovFoOoasH2HaY'
response = SpotifyService.SpotifySession.artist_albums(artist_id=CalvinHarris_uri)
albums = response['items']
while response['next']:
    response = SpotifyService.SpotifySession.next(response)
    albums.extend(response['items'])
for album in albums:
    print(album['name'])
