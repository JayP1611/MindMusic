import requests
from src.spotify.auth import SpotifyAuth

class SpotifyClient:
    def __init__(self):
        self.auth = SpotifyAuth()

    def _headers(self):
        token = self.auth.get_access_token()
        return {"Authorization": f"Bearer {token}", "User-Agent": "mood-to-playlist/1.0 (contact: pawarjay1611@gmail.com)"}

    def search_tracks(self, query: str, limit: int = 20, market: str = "AU"):
        """
        Search tracks by query string
        """
        url = "https://api.spotify.com/v1/search"
        params = {"q": query,
                  "type": "track",
                  "limit": limit,
                  "market": market
                  }
        resp = requests.get(url, headers = self._headers(), params = params, timeout = 30)
        resp.raise_for_status()
        return resp.json()['tracks']['items']

# Test code
if __name__ == "__main__":
    sp = SpotifyClient()
    results = sp.search_tracks(query="calm study", limit = 10)
    for i, track in enumerate(results, 1):
        print(f"{i}. {track['name']} - {track['artists'][0]['name']}")
        print(f"{i}. {track}")
