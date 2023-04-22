from services_sessions.spotify_service import spotify_session as spotify

# TODO Create a class to convert playlists
# TODO Treat errors

# List all playlist and get ids
playlists_items = dict()
limit_user_playlists = 50
offset_user_playlists = 0

user_playlists_response = spotify.current_user_playlists(limit=limit_user_playlists, offset=offset_user_playlists)

if user_playlists_response.get('error'):
    print('There was an error in the user playlist request')
else:
    playlists_items = user_playlists_response['items'][0]
    while user_playlists_response['next'] is not None:
        offset_user_playlists += limit_user_playlists
        user_playlists_response = spotify.current_user_playlists(limit=limit_user_playlists,
                                                                 offset=offset_user_playlists)
        print(user_playlists_response['items'][0])
        if user_playlists_response.get('items'):
            playlists_items = {**playlists_items, **user_playlists_response['items'][0]}

print(playlists_items)