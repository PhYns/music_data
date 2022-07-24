import sys
import os
import tidalapi
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(base_dir))
from Credentials import TidalCredentials

# Create Tidal Session
TidalSession = tidalapi.Session()
TidalSession.country_code = "BR"
TidalSession.load_oauth_session(session_id=TidalCredentials.session_id,token_type=TidalCredentials.token_type,access_token=TidalCredentials.access_token)
if not TidalSession.check_login():
    print("Tidal Session expired, please login again")
    TidalSession.login_oauth_simple()
    TidalCredentials.access_token = TidalSession.access_token
    TidalCredentials.session_id = TidalSession.session_id
    TidalCredentials.token_type = TidalSession.token_type