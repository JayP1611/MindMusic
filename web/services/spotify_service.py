from typing import List, Dict
from src.spotify.search import search_from_tags
from src.recommender.ranker import rank_by_popularity

def get_ranked_tracks(tags: List[str], limit_candidates: int = 50, top_n: int = 20) -> List[Dict]:
    candidates = search_from_tags(tags, limit=limit_candidates)
    ranked = rank_by_popularity(candidates, top_n=top_n)
    return ranked
