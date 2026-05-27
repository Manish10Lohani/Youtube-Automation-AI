"""
Video creation with MoviePy (v2.x).

This version:
- Uses a static background image based on genre (if found)
- Falls back to black screen if image is missing
- Attaches the generated audio as the soundtrack
"""

from pathlib import Path

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip, ColorClip


def create_video_from_audio(
    audio_path: Path,
    output_path: Path,
    genre: str = "horror",
    fps: int = 24,
) -> Path:
    """
    Create a simple video with:
    - a static background image (selected by genre)
    - the given audio as soundtrack

    :param audio_path: Path to the .mp3 file
    :param output_path: Path to the .mp4 file
    :param genre: "horror", "tech", "psychology", "motivational", "educational"
    :param fps: frames per second
    """
    audio_path = Path(audio_path)
    output_path = Path(output_path)

    print(f"[DEBUG] Loading audio from: {audio_path}")
    audio_clip = AudioFileClip(str(audio_path))
    duration = audio_clip.duration
    print(f"[DEBUG] Audio duration: {duration:.2f} seconds")

    # Map genre to background image
    bg_map = {
        "horror": Path("assets/backgrounds/horror.jpg"),
        "tech": Path("assets/backgrounds/tech.jpg"),
        "psychology": Path("assets/backgrounds/psychology.jpg"),
        "motivational": Path("assets/backgrounds/motivational.jpg"),
        "educational": Path("assets/backgrounds/educational.jpg"),
    }

    genre_key = genre.strip().lower()
    bg_path = bg_map.get(genre_key, bg_map["horror"])

    # Build visual clip
    if bg_path.exists():
        print(f"[DEBUG] Using background image: {bg_path}")
        video_clip = ImageClip(str(bg_path), duration=duration)
    else:
        print(f"[WARN] Background image not found at {bg_path}, using plain black screen.")
        # 1280x720 black background
        video_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)

    # Attach audio
    video_with_audio = video_clip.with_audio(audio_clip)

    # Ensure output folder exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"[DEBUG] Writing video to: {output_path}")
    video_with_audio.write_videofile(
        str(output_path),
        fps=fps,
        codec="libx264",
        audio=True,
        audio_fps=44100,
        audio_codec="aac",
    )

    # Cleanup
    audio_clip.close()
    video_clip.close()
    video_with_audio.close()

    print(f"[OK] Video created at: {output_path}")
    return output_path


if __name__ == "__main__":
    # Optional manual test
    demo_audio = Path("data/processed/audio/demo_voiceover.mp3")
    out_video = Path("data/processed/video/demo_video_with_bg.mp4")

    if not demo_audio.exists():
        print("Demo audio not found. Run voiceover_generator test first.")
    else:
        create_video_from_audio(
            audio_path=demo_audio,
            output_path=out_video,
            genre="horror",
        )
        print(f"Saved demo video to: {out_video}")
