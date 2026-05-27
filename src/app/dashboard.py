import streamlit as st
from pathlib import Path
import base64
import sys

# ---- Path + imports ----
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.main import run_pipeline
from src.automation.topic_suggester import suggest_topics


# ---- Styling helpers ----
def set_background(image_path):
    """Set full-page background image using base64 CSS."""
    img_path = Path(image_path)

    # Debug info (remove later if you want)
    st.write(f"🔍 Background path: {img_path} (exists: {img_path.exists()})")

    if not img_path.exists():
        st.warning("Background image not found. Check assets/bg.jpg path.")
        return

    with open(img_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    css = f"""
    <style>
    body {{
        background: none;
    }}

    .stApp {{
        background: url("data:image/jpg;base64,{encoded}") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def set_glass_effect():
    """Apply glassmorphism to main container and sidebar."""
    css = """
    <style>
    .block-container {
        backdrop-filter: blur(18px);
        background: rgba(0, 0, 0, 0.30);
        padding: 2.5rem 2rem;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    section[data-testid="stSidebar"] > div:first-child {
        backdrop-filter: blur(14px);
        background: rgba(0, 0, 0, 0.65);
        border-right: 1px solid rgba(255, 255, 255, 0.12);
    }

    h1, h2, h3, h4, h5, h6, p, label {
        color: #f5f5f5 !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# ---- Page config ----
st.set_page_config(
    page_title="YouTube Automation AI",
    page_icon="🎬",
    layout="wide",
)

set_background(ROOT_DIR / "assets" / "bg.jpg")
set_glass_effect()

st.title("🎬 YouTube Automation AI Studio")
st.caption("Generate scripts, audio, video & subtitles for your YouTube automation channel.")


# ---- Defaults to prevent NameError ----
generate_btn = False
genre = "horror"
niche = ""
topic = ""
tone = "storytelling"
minutes = 8


# ---------------- SIDEBAR: CONTROLS ---------------- #
with st.sidebar:
    st.header("⚙️ Video Settings")

    genre = st.selectbox(
        "Content genre",
        ["horror", "tech", "psychology", "motivational", "educational"],
        index=0,
        help="This influences the script style and background visuals.",
    )

    niche = st.text_input(
        "Channel niche",
        value="",
        placeholder="e.g., horror stories, tech reviews, psychology tips",
        help="Describe what type of channel this video is for.",
    )

    # Topic in session state
    if "topic_value" not in st.session_state:
        st.session_state["topic_value"] = ""

    topic = st.text_input(
        "Video topic",
        value=st.session_state["topic_value"],
        placeholder="e.g., True scary story from a nurse working night shift",
        help="What should this specific video be about?",
    )
    st.session_state["topic_value"] = topic

    tone = st.selectbox(
        "Narration tone",
        ["storytelling", "casual", "dramatic"],
        index=0,
        help="Affects how the script is written.",
    )

    minutes = st.slider(
        "Target length (minutes)",
        min_value=1,
        max_value=15,
        value=8,
        help="Approximate duration of the video.",
    )

    # ---- Topic Suggestions ----
    st.markdown("### 💡 Topic Ideas")
    suggest_btn = st.button("✨ Suggest Topics", use_container_width=True)

    if suggest_btn:
        suggestions = suggest_topics(
            genre=genre,
            niche=niche,
            tone=tone,
            topic_seed=topic,
            count=8,
        )
        st.session_state["topic_suggestions"] = suggestions.topics

    if "topic_suggestions" in st.session_state:
        for i, s in enumerate(st.session_state["topic_suggestions"], start=1):
            if st.button(f"{i}. {s}", key=f"sugg_{i}", use_container_width=True):
                st.session_state["topic_value"] = s
                st.rerun()

    st.markdown("---")
    generate_btn = st.button("🚀 Generate Video", use_container_width=True)


# ---------------- MAIN AREA: OUTPUT ---------------- #
if not generate_btn:
    st.info("Configure your video in the sidebar and click **“🚀 Generate Video”** to start.")
else:
    # use latest topic value (in case suggestion was clicked)
    topic = st.session_state.get("topic_value", "").strip()

    if not topic:
        st.error("Please enter a video topic before generating.")
    else:
        st.info("Running the full pipeline… This may take a bit (script, audio, video, subtitles).")

        with st.spinner("Generating script, metadata, audio, video, and subtitles…"):
            try:
                result = run_pipeline(
                    niche=niche,
                    topic=topic,
                    tone=tone,
                    minutes=minutes,
                    genre=genre,
                )
            except Exception as e:
                st.error(f"❌ Something went wrong while generating the video: {e}")
                st.stop()

        st.success("✅ Done! Your video package has been generated.")

        # Unpack result
        title: str = result["title"]
        script_text: str = result["script"]
        outline_text: str = result["outline"]
        metadata = result["metadata"]
        thumbnail_spec = result["thumbnail_spec"]
        audio_path: Path = result["audio_path"]
        video_path: Path = result["video_path"]
        subtitles_path: Path = result["subtitles_path"]

        tab_overview, tab_script, tab_media, tab_files = st.tabs(
            ["📌 Overview", "📖 Script", "🎧 / 🎬 Media", "📂 Paths"]
        )

        with tab_overview:
            st.subheader("📌 Generated Title")
            st.markdown(f"### {title}")

            st.subheader("📝 YouTube Description")
            st.text_area("Description", value=metadata.get("description", ""), height=200)

            st.subheader("🏷️ Tags")
            tags = metadata.get("tags", [])
            st.write(", ".join(tags) if tags else "_No tags generated._")

            st.subheader("🖼️ Thumbnail Text & Prompt")
            st.write(f"**Thumbnail text:** {thumbnail_spec.text}")
            st.caption(f"Prompt idea for an image model:\n\n{thumbnail_spec.prompt}")

        with tab_script:
            st.subheader("📖 Full Script")
            st.text_area("Script", value=script_text, height=350)

            st.subheader("🧱 Outline")
            st.text(outline_text)

        with tab_media:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🎧 Voiceover Preview")
                st.write(str(audio_path))
                if audio_path.exists():
                    st.audio(audio_path.read_bytes(), format="audio/mp3")
                else:
                    st.warning("Audio file not found on disk.")

            with col2:
                st.subheader("🎬 Video Preview")
                st.write(str(video_path))
                if video_path.exists():
                    st.video(str(video_path))
                else:
                    st.warning("Video file not found on disk.")

            st.markdown("---")
            st.subheader("📝 Subtitles (.srt)")
            st.write(str(subtitles_path))
            st.caption("Upload this .srt with your video to YouTube or open in VLC to see subtitles.")

        with tab_files:
            st.subheader("📂 Generated File Paths")
            st.markdown(f"- **Audio (MP3):** `{audio_path}`")
            st.markdown(f"- **Video (MP4):** `{video_path}`")
            st.markdown(f"- **Subtitles (SRT):** `{subtitles_path}`")
            st.markdown("Use these paths in File Explorer to locate your outputs.")
