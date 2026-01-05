from typing import List, Dict

def rank_by_popularity(candidates: List[Dict], top_n: int = 30) -> List[Dict]:
    """
    :param candidates:
    :param top_n:
    :return: Sort tracks by Spotify popularity (0-100), higher is better.
    """
    candidates = [c for c in candidates if c.get("id")]
    candidates.sort(key=lambda x: int(x.get("popularity", 0)), reverse=True)
    return candidates[:top_n]

