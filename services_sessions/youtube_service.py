from ytmusicapi import setup, YTMusic
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from credentials.ytm_headers import headers_captured

# Create file for auth
if not os.path.exists("../credentials/youtube_credentials.json"):
    setup(filepath="../credentials/youtube_credentials.json", headers_raw=headers_captured)

# Create instance with authentication
ytm_session = YTMusic("../credentials/youtube_credentials.json")
