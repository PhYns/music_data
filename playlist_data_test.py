from services_sessions.spotify_service import SpotifySession



# Test get all playlist data
spotify = SpotifySession()
print(spotify.get_all_playlists_data())
