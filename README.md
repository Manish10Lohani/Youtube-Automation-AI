# 🎬 YouTube Automation AI

An end-to-end AI-powered pipeline that takes a topic and genre, then automatically generates a script, voiceover, video, subtitles, and YouTube metadata — all from a single Streamlit interface.

\---

!\[YouTube Automation AI Studio](assets/backgrounds/demo.png)

## 🚀 Features

* **Script generation** — genre and tone-aware narration scripts
* **Topic suggestions** — auto-generates relevant video ideas
* **Voiceover** — converts scripts to MP3 using text-to-speech
* **Video creation** — assembles MP4 with genre-matched background and audio
* **Subtitle generation** — proportional-timing SRT files synced to audio
* **YouTube metadata** — titles, descriptions, tags, and CTAs ready to copy

\---

## 🛠 Tech Stack

|Tool|Purpose|
|-|-|
|Python 3.10+|Core language|
|Streamlit|Web UI dashboard|
|MoviePy|Video and audio processing|
|gTTS|Text-to-speech voiceover|
|LLM API (pluggable)|Script and metadata generation|

\---

## 📁 Project Structure

```
YouTube-Automation-AI/
├── src/
│   ├── app/
│   │   └── dashboard.py          # Streamlit UI
│   ├── api/
│   │   └── llm\_script\_generator.py  # LLM integration
│   └── automation/
│       ├── voiceover\_generator.py
│       ├── video\_creator.py
│       ├── subtitles\_generator.py
│       ├── metadata\_generator.py
│       ├── thumbnail\_text\_generator.py
│       └── topic\_suggester.py
├── assets/
│   └── backgrounds/              # Genre-specific background images
├── data/
│   └── processed/                # Generated audio, video, subtitles
├── requirements.txt
└── .env                          # API keys (not committed)
```

\---

## ⚙️ Setup \& Installation

```bash
# 1. Clone the repo
git clone https://github.com/Manish10Lohani/Youtube-Automation-AI.git
cd Youtube-Automation-AI

# 2. Create and activate a virtual environment
python -m venv venv
venv\\Scripts\\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys
cp .env.example .env
# Edit .env with your LLM API key

# 5. Run the app
streamlit run src/app/dashboard.py
```

\---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
LLM\_API\_KEY=your\_api\_key\_here
```

\---

## 🎯 How It Works

1. Enter a **topic** and select a **genre** in the Streamlit UI
2. The pipeline generates a **script** using the LLM API
3. The script is converted to an **MP3 voiceover**
4. A **video** is assembled with a genre-matched background
5. **SRT subtitles** are generated proportional to audio timing
6. **YouTube metadata** (title, description, tags) is ready to copy

\---

## 📌 Requirements

See `requirements.txt`. Key dependencies:

* `streamlit`
* `moviepy`
* `gTTS`
* `python-dotenv`

\---

## 📄 License

MIT License — feel free to use and modify.

