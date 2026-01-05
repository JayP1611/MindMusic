from src.spotify.search import search_from_tags
from src.recommender.ranker import rank_by_popularity

if __name__ == "__main__":
    tags = ["happy", "happy", "depression", "mellow"]

    candidates = search_from_tags(tags, limit = 50)   # get more, rank better
    ranked = rank_by_popularity(candidates, top_n = 15)

    for i, t in enumerate(ranked, 1):
        print(f"{i}. {t['name']} — {t['artists']} | popularity={t['popularity']} | {t['spotify_url']}")
