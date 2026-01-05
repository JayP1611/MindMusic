import json
from flask import Flask, render_template, request, redirect, url_for, flash

from web.db import Base, engine, SessionLocal
from web.models import PromptRun, Generation, Recommendation
from web.services.generator_service import generate_structured
from web.services.spotify_service import get_ranked_tracks

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = "dev-secret-change-me"

# Create tables if not exist
Base.metadata.create_all(bind=engine)

EMOJI = {
    "headphones": "🎧",
    "notes": "✨",
    "sparkle": "🎶",
    "orange": "🧡",
    "star": "⭐"
}

@app.get("/")
def index():
    return render_template("index.html",
                           EMOJI = EMOJI)

@app.post("/generate")
def generate():
    user_prompt = request.form.get("prompt", "").strip()
    if not user_prompt:
        flash("Please enter a prompt.")
        return redirect(url_for("index"))

    gen = generate_structured(user_prompt)
    tracks = get_ranked_tracks(gen["tags"], limit_candidates=50, top_n=20)

    return render_template(
        "result.html",
        prompt=user_prompt,
        title=gen["title"],
        tags=gen["tags"],
        description=gen["description"],
        tracks=tracks,
        raw_text=gen.get("raw_text", "")
    )

@app.post("/save")
def save():
    user_prompt = request.form.get("prompt", "").strip()
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    tags_json = request.form.get("tags_json", "[]")
    tracks_json = request.form.get("tracks_json", "[]")

    tags = json.loads(tags_json)
    tracks = json.loads(tracks_json)

    db = SessionLocal()
    try:
        pr = PromptRun(prompt_text=user_prompt)
        db.add(pr)
        db.flush()  # get pr.id

        gen = Generation(
            prompt_run_id=pr.id,
            title=title,
            description=description,
            tags_json=json.dumps(tags),
            model_version="gpt2_finetuned",
        )
        db.add(gen)
        db.flush()  # get gen.id

        for idx, t in enumerate(tracks, start=1):
            rec = Recommendation(
                generation_id=gen.id,
                track_id=t["id"],
                track_name=t["name"],
                artists=t["artists"],
                spotify_url=t["spotify_url"],
                popularity=int(t.get("popularity", 0)),
                rank=idx
            )
            db.add(rec)

        db.commit()
        flash("Saved successfully!")
        return redirect(url_for("history"))
    except Exception as e:
        db.rollback()
        flash(f"Save failed: {e}")
        return redirect(url_for("index"))
    finally:
        db.close()

@app.get("/history")
def history():
    db = SessionLocal()
    try:
        rows = (
            db.query(Generation)
            .order_by(Generation.created_at.desc())
            .limit(30)
            .all()
        )

        items = []
        for g in rows:
            items.append({
                "id": g.id,
                "title": g.title,
                "description": g.description,
                "tags": json.loads(g.tags_json),
                "created_at": g.created_at,
            })
        return render_template("history.html", items=items)
    finally:
        db.close()

@app.get("/history/<int:generation_id>")
def history_detail(generation_id: int):
    db = SessionLocal()
    try:
        gen = db.query(Generation).filter(Generation.id == generation_id).first()
        if not gen:
            flash("Not found.")
            return redirect(url_for("history"))

        tracks = (
            db.query(Recommendation)
            .filter(Recommendation.generation_id == generation_id)
            .order_by(Recommendation.rank.asc())
            .all()
        )

        return render_template(
            "result.html",
            prompt=gen.prompt_run.prompt_text if gen.prompt_run else "",
            title=gen.title,
            tags=json.loads(gen.tags_json),
            description=gen.description,
            tracks=[{
                "id": t.track_id,
                "name": t.track_name,
                "artists": t.artists,
                "spotify_url": t.spotify_url,
                "popularity": t.popularity
            } for t in tracks],
            raw_text=""
        )
    finally:
        db.close()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
