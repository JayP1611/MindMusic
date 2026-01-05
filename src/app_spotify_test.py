from src.spotify.search import search_from_tags

if __name__ == "__main__":
    tags = ["study", "calm", "hopeful", "focus"]
    tracks = search_from_tags(tags, limit = 10)

    for i, t in enumerate(tracks, start = 1):
        print(f"{i}. {t["name"]} - {t['artists']} | {t['spotify_url']}")