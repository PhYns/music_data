import datetime
import sys
import os
import tidalapi

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(base_dir))
from credentials import tidal_credentials as credentials

# Create Tidal Session
tidal_session = tidalapi.Session()
tidal_session.country_code = "BR"
if credentials.expiration_date > datetime.date.today():
    tidal_session.load_oauth_session(token_type=credentials.token_type, access_token=credentials.access_token,
                                 tidal_session=credentials.session_id)
if not tidal_session.check_login():
    print("Tidal Session expired, please login again")
    tidal_session.login_oauth_simple()
    credentials.access_token = tidal_session.access_token
    credentials.session_id = tidal_session.session_id
    credentials.token_type = tidal_session.token_type
    credentials.expiration_date = tidal_session.expiry_time
