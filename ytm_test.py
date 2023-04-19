from services_sessions.youtube_service import ytm_session

# Test YoutubeMusic API
playlistId = ytm_session.create_playlist("test", "test description")
search_results = ytm_session.search("Oasis Wonderwall")
ytm_session.add_playlist_items(playlistId, [search_results[0]['videoId']])