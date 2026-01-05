# 🎧 MindMusic

**MindMusic** is an AI-powered, mood-aware music recommendation web application that generates personalized playlists based on how a user feels. It combines Natural Language Processing (NLP), a fine-tuned GPT-2 model, and Spotify’s API to deliver emotionally intelligent music recommendations.

---

## 🚀 What MindMusic Does
- 🧠 Understands user mood from free-text input  
- 🎵 Generates context-aware music recommendations  
- 🤖 Uses a fine-tuned GPT-2 model for text understanding  
- 🎧 Integrates with Spotify to fetch real tracks  
- 🌐 Provides a clean, Flask-based web interface  

---

## 🧩 System Architecture
1. **User Input** – User describes their mood in natural language  
2. **NLP Layer** – A fine-tuned GPT-2 model interprets emotional context and intent  
3. **Query Generation** – Semantic music descriptors (Title, Tags, Description) are generated  
4. **Spotify API** – Tracks are retrieved using Spotify search endpoints. The id, track namae, artists, album, spotify URL and popularity are retrieved with the help of Spotify API.   
5. **Ranking** – Tracks are ranked using Spotify-provided popularity scores  
6. **Web App (Flask)** – Recommendations are rendered in a clean UI  

---

## 🎥 Demo
A full working demo of the application is included in this repository:

👉 **MindMusic.mp4**

This video demonstrates:
- Mood input
- Playlist generation
- End-to-end application flow
- Code in the project

---

## 🛠️ Tech Stack
**Backend & AI**
- Python
- Flask
- GPT-2 (fine-tuned)
- Hugging Face Transformers
- Custom ranking & recommendation logic

**APIs & Services**
- Spotify Web API

**Frontend**
- HTML / CSS (Jinja templates)

**Database**
- SQLAlchemy (SQLite / MySQL compatible)

---

## 📂 Project Structure

```text
MindMusic/
├── src/                 # NLP, model training & recommendation logic
├── web/                 # Flask app, services, templates & static files
├── MindMusic.mp4        # Demo video
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
└── .gitignore
```
---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/JayP1611/MindMusic.git
cd MindMusic
```

### 2️⃣ Create virtual environment
python -m venv .venv
```base
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install dependencies
```base
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables
Create a .env file using .env.example:
```base
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

5️⃣ Run the web app
```base
python web/app.py
```
Open: http://127.0.0.1:5000

👤 Author
Jay Pawar 
Master of Data Science — Deakin University
Interests: Data Science, Machine Learning, Data Analytics, API Development, Database Management, Mathematics and Statistics for AI, AI Systems, Data Engineering

⭐ If you like this project, feel free to star the repository!
