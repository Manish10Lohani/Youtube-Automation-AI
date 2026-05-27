"""
Generate improved .srt subtitles:

- Splits script into sentences
- Computes timing proportional to sentence length
- Matches speaking pace more closely
"""

from pathlib import Path
import re
from typing import List
from moviepy.audio.io.AudioFileClip import AudioFileClip


def _split_into_sentences(text: str) -> List[str]:
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]


def _format_timestamp(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    ms = int((seconds - int(seconds)) * 1000)
    s = int(seconds) % 60
    m = (int(seconds) // 60) % 60
    h = int(seconds) // 3600
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def create_srt_from_script(script: str, audio_path: Path, output_path: Path) -> Path:
    audio_path = Path(audio_path)
    output_path = Path(output_path)

    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    # Load audio to get total duration
    audio_clip = AudioFileClip(str(audio_path))
    duration = audio_clip.duration
    audio_clip.close()

    sentences = _split_into_sentences(script)

    if not sentences:
        output_path.write_text("")
        return output_path

    # Count total words
    def count_words(s: str):
        return len(re.findall(r'\w+', s))

    sentence_word_counts = [count_words(s) for s in sentences]
    total_words = sum(sentence_word_counts)

    # Compute duration per sentence
    lines = []
    current_time = 0.0

    for idx, sentence in enumerate(sentences, start=1):
        word_count = sentence_word_counts[idx - 1]

        # Time proportional to sentence length
        sentence_duration = (word_count / total_words) * duration

        start_ts = _format_timestamp(current_time)
        end_ts = _format_timestamp(current_time + sentence_duration)

        block = f"{idx}\n{start_ts} --> {end_ts}\n{sentence}\n"
        lines.append(block)

        current_time += sentence_duration

    # Write .srt file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"[OK] Improved subtitles written to: {output_path}")
    return output_path
