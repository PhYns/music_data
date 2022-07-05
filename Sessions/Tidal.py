import tidalapi

# Create Tidal Session
TidalSession = tidalapi.Session()
TidalSession.login_oauth_simple()
TidalSession.country_code = 'BR'
