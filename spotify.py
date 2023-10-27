import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'your_redirect_uri'

# Initialize the Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

# Define the URI of the "Ram Siya Ram" track
track_uri = 'spotify:track:YOUR_TRACK_URI'

# Play the specified track
sp.start_playback(uris=[track_uri])
