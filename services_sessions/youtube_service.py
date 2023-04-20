import os
import sys
from ytmusicapi import setup, YTMusic
SCRIPT_DIR = os.path.dirname(os.path.abspath(__name__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from services_sessions.credentials.ytm_headers import headers_captured

# Create file for auth
if not os.path.exists("services_sessions/credentials/youtube_credentials.json"):
    setup(filepath="services_sessions/credentials/youtube_credentials.json", headers_raw=headers_captured)

# Create instance with authentication
ytm_session = YTMusic("services_sessions/credentials/youtube_credentials.json")
