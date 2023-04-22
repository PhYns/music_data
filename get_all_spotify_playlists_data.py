from services_sessions.spotify_service import spotify_session as spotify

# List all playlist and get data from them
playlists_data = list()
limit_user_playlists: int = 50
offset_user_playlists: int = 0

# Make first request
user_playlists_response: dict = spotify.current_user_playlists(limit=limit_user_playlists, offset=offset_user_playlists)
# Catch error
if user_playlists_response.get('error'):
    print('There was an error in the user playlist request')
else:
    # Save playlist data
    playlists_data.extend(user_playlists_response['items'])
    # Check if there is more pages, if there is make other requests and save data
    while user_playlists_response['next'] is not None:
        offset_user_playlists += limit_user_playlists
        user_playlists_response = spotify.current_user_playlists(limit=limit_user_playlists,
                                                                 offset=offset_user_playlists)
        if user_playlists_response.get('items'):
            playlists_data.extend(user_playlists_response['items'])

print(*playlists_data, sep='\n')
