from services_sessions import youtube_service

# Test YoutubeMusic API
playlistId = youtube_service.ytm_session.create_playlist("test", "test description")
print(playlistId)
search_results = youtube_service.ytm_session.search("Oasis Wonderwall")
print(search_results)
youtube_service.ytm_session.add_playlist_items(playlistId, [search_results[0]['videoId']])
