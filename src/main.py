"""
Master pipeline for YouTube Automation AI.

Steps:
1. Generate script (LLM or fallback)
2. Generate metadata (description, tags, etc.)
3. Generate thumbnail text + prompt
4. Generate voiceover (MP3)
5. Generate subtitles (.srt)
6. Create simple video (MP4 with audio + background)
"""

from pathlib import Path

from dotenv import load_dotenv
from src.automation.subtitles_generator import create_srt_from_script
from src.api.llm_script_generator import generate_script
from src.automation.metadata_generator import generate_metadata
from src.automation.thumbnail_text_generator import generate_thumbnail_spec
from src.automation.voiceover_generator import generate_voiceover
from src.automation.video_creator import create_video_from_audio

load_dotenv()

# Base folders
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"


def run_pipeline(
    niche: str,
    topic: str,
    tone: str = "storytelling",
    minutes: int = 8,
    genre: str = "horror",
):
    """
    Run the full pipeline:
    - Script
    - Metadata
    - Thumbnail text
    - Voiceover
    - Subtitles
    - Video
    """

    # 1 – Script
    print("\n[1] Generating script...")
    script_result = generate_script(
        topic=topic,
        tone=tone,
        target_duration_minutes=minutes,
        genre=genre,
    )
    title = script_result["title"]
    full_script = script_result["full_script"]
    print(f"[+] Title: {title}")

    # 2 – Metadata
    print("\n[2] Generating metadata...")
    metadata = generate_metadata(
        title=title,
        topic=topic,
        niche=niche,
        script=full_script,
    )

    # 3 – Thumbnail text / prompt
    thumb_spec = generate_thumbnail_spec(title, niche)

    print("[+] Description preview:")
    print(metadata["description"][:200], "...")
    print("[+] Tags:", ", ".join(metadata["tags"][:8]), "...")

    # 4 – Voiceover
    print("\n[3] Generating voiceover (MP3)...")
    audio_path = PROCESSED_DIR / "audio" / "main_voiceover.mp3"
    audio_path.parent.mkdir(parents=True, exist_ok=True)
    generate_voiceover(full_script, output_path=audio_path)
    print(f"[+] Voiceover saved to: {audio_path}")

    # 5 – Subtitles (.srt)
    print("\n[4] Generating subtitles (.srt)...")
    video_path = PROCESSED_DIR / "video" / "main_video.mp4"
    subtitles_path = video_path.with_suffix(".srt")
    subtitles_path.parent.mkdir(parents=True, exist_ok=True)
    create_srt_from_script(
        script=full_script,
        audio_path=audio_path,
        output_path=subtitles_path,
    )

    # 6 – Video
    print("\n[5] Creating video (MP4) with audio...")
    create_video_from_audio(
        audio_path=audio_path,
        output_path=video_path,
        genre=genre,
    )
    print(f"[+] Video saved to: {video_path}")

    print("\n✅ Pipeline finished!")

    return {
        "title": title,
        "script": script_result["full_script"],
        "outline": script_result["outline"],
        "metadata": metadata,
        "thumbnail_spec": thumb_spec,      
        "audio_path": audio_path,
        "video_path": video_path,
        "subtitles_path": subtitles_path,
    }


if __name__ == "__main__":
    # You can change these defaults
    niche_input = "horror stories"
    topic_input = "True scary story from a nurse working night shift"
    tone_input = "storytelling"
    genre_input = "horror"

    run_pipeline(
        niche=niche_input,
        topic=topic_input,
        tone=tone_input,
        minutes=8,
        genre=genre_input,
    )
