from typing import List, Dict
from src.spotify.client import SpotifyClient

def build_query_from_stage(tags: List[str]) -> str:
    """
    Convert tags to a SPOTIFY search query.
    Simple and effective: join important tags and common study vibe terms
    """

    tags = [t.strip() for t in tags if t and t.strip()]

    core = tags[:4]
    return " ".join(core)

def search_from_tags(tags: List[str], limit: int = 30) -> List[Dict]:
    sp = SpotifyClient()
    q = build_query_from_stage(tags)
    items = sp.search_tracks(query = q, limit = min(limit, 50))

    # Keep only fields we care about now
    tracks = []
    for t in items:
        tracks.append({
            "id": t["id"],
            "name": t["name"],
            "artists": ", ".join(a["name"] for a in t["artists"]),
            "album": t["album"]["name"],
            "spotify_url": t["external_urls"]["spotify"],
            "popularity": t["popularity"]
        })
    return tracks

# Test code
# if __name__ == "__main__":
#     # Example public Spotify track IDs
#     test_track_ids = [
#         "3n3Ppam7vgaVa1iaRUc9Lp",  # Mr. Brightside
#         "7ouMYWpwJ422jRcDASZB7P",  # Numb
#         "0eGsygTp906u18L0Oimnem",  # Fix You
#     ]
#     print(search_from_tags(test_track_ids))
