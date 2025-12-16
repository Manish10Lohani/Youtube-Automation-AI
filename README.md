# 🎬 YouTube Automation AI

An end-to-end AI-powered YouTube automation tool that generates:
- Video scripts (genre & tone aware)
- Topic suggestions
- Voiceovers (TTS)
- Videos (MP4)
- Subtitles (SRT)
- YouTube metadata (title, description, tags)

Built with Python and Streamlit.

---

## 🚀 Features
- Genre-based script generation
- Topic suggestion engine
- Automatic voiceover generation
- Video creation with audio
- Subtitle generation (.srt)
- Modern Streamlit UI
- Fallback logic when LLM APIs fail

---

## 🛠 Tech Stack
- Python
- Streamlit
- MoviePy
- LLM APIs (pluggable)
- Text-to-Speech
- Subtitle generation

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/youtube-automation-ai.git
cd youtube-automation-ai
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run src/app/dashboard.py
