import spotipy, os

SpotifyCredentials = spotipy.oauth2.SpotifyClientCredentials(os.environ['CLIENT_ID_GITSECRET'], os.environ['CLIENT_SECRET_GITSECRET'])