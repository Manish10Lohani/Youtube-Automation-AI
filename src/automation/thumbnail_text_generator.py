"""
Thumbnail text + prompt generator.

This does NOT create the actual image yet.
It just decides:
- What short text goes on the thumbnail
- What prompt you could send to an AI image model
"""

from dataclasses import dataclass


@dataclass
class ThumbnailSpec:
    text: str
    prompt: str
    style: str = "dark, high contrast, bold typography"


def generate_thumbnail_spec(title: str, niche: str) -> ThumbnailSpec:
    """
    Generate short thumbnail text and a prompt for image generation.
    """

    # Shorten very long titles for thumbnail text
    if len(title) > 45:
        thumb_text = title[:42].rstrip() + "..."
    else:
        thumb_text = title

    prompt = (
        f"Create a dramatic YouTube thumbnail for a {niche} video titled '{title}'. "
        "Use bold text, dark background and cinematic lighting."
    )

    return ThumbnailSpec(text=thumb_text, prompt=prompt)


if __name__ == "__main__":
    spec = generate_thumbnail_spec(
        title="True Scary Story From A Nurse Working Night Shift",
        niche="horror stories",
    )
    print("THUMBNAIL TEXT:", spec.text)
    print("IMAGE PROMPT:", spec.prompt)
