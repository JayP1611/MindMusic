import base64
import time
import requests
from src.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

class SpotifyAuth:
    """
    Spotify client credentials authentication.
    Good for search + audio features. Not enough to create playlist for a user
    """
    def __init__(self):
        self._token = None
        self._expires_at = None

    def get_access_token(self) -> str:
        now = int(time.time())
        if (self._token and now < self._expires_at - 30):
            return self._token

        auth_header = base64.b64encode(
            f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode("utf-8")
        ).decode("utf-8")

        resp = requests.post(
            "https://accounts.spotify.com/api/token",
            headers = {
                "Authorization": f"Basic {auth_header}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data = {"grant_type": "client_credentials"},
            timeout = 30,
        )
        resp.raise_for_status()
        data = resp.json()

        self._token = data["access_token"]
        self._expires_at = now + int(data.get("expires_in", 3600))
        return self._token

if __name__ == "__main__":
    from src.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
    print("Client ID loaded: ", SPOTIFY_CLIENT_ID)
    print("Client secret loaded: ", SPOTIFY_CLIENT_SECRET)

    auth = SpotifyAuth()
    token = auth.get_access_token()
    print("Access token: ", token)