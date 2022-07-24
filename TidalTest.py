import sys
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(base_dir))
from ServicesSessions.TidalService import TidalSession as Tidal

Tidal.user.playlists()
# Tidal.get_user_playlists()