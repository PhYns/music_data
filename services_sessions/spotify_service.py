import spotipy.client
from spotipy import oauth2, Spotify
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from services_sessions.credentials import spotify_credentials as credentials


class SpotifySession:
    def __init__(self, client_id=credentials.ClientId, client_secret=credentials.ClientSecret):
        # TODO treat auth error
        """
        Initializes spotify session
        """ 
        # Checking if there is a credential file
        try:
            client_id
            client_secret
        except NameError:
            print("Credentials missing\nYou have to get your credentials in your spotify developer portal and use them\
            here.")
        else:
            # Create Spotify Session
            scope = ["user-library-read", "user-read-currently-playing", "playlist-modify-private",
                     "user-follow-modify",
                     "user-library-modify", "playlist-read-private"]
            self.spotify_session = Spotify(auth_manager=oauth2.SpotifyOAuth(client_id=credentials.ClientId,
                                                                            client_secret=credentials.ClientSecret,
                                                                            redirect_uri="https://localhost/",
                                                                            scope=scope))
            
    def get_session(self):
        """
        Return the created session itself
        :rtype: spotipy.client.Spotify
        """
        return self.spotify_session
    
    def get_all_playlists_data(self):
        """
        Returns all the data of all playlists
        :rtype: list
        """
        # List all playlists from the current user and get all data from them
        playlists_data = list()
        limit_user_playlists: int = 50
        offset_user_playlists: int = 0

        # Make first request
        user_playlists_response: dict = self.spotify_session.current_user_playlists(limit=limit_user_playlists,
                                                                                    offset=offset_user_playlists)
        # Catch error
        if user_playlists_response.get('error'):
            print("There was an error in the user playlist request")
        else:
            # Save playlist data
            playlists_data.extend(user_playlists_response['items'])
            # Check if there is more pages, if there is make other requests and save data
            while user_playlists_response['next'] is not None:
                offset_user_playlists += limit_user_playlists
                user_playlists_response = self.spotify_session.current_user_playlists(limit=limit_user_playlists,
                                                                                      offset=offset_user_playlists)
                if user_playlists_response.get('items'):
                    playlists_data.extend(user_playlists_response['items'])

        return playlists_data
