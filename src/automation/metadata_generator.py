"""
Generates YouTube metadata: description, tags, keywords, CTA.
"""

from typing import Dict, List, Union


def generate_metadata(
    title: str,
    topic: str,
    niche: str,
    script: str,
) -> Dict[str, Union[str, List[str]]]:
    """
    Simple rule-based metadata generator.

    Later, you can replace parts of this with an LLM call if you want
    smarter SEO descriptions or tags.
    """

    # Description: short intro + CTA
    description = (
        f"{title}\n\n"
        f"In this video, we explore {topic} in the {niche} niche. "
        "Stay till the end for the full story!\n\n"
        "👉 If you enjoy this video, please like, share, and subscribe.\n"
    )

    # Keywords / tags: based on niche, topic, and words from the title
    base_keywords = [
        niche,
        topic,
        "YouTube automation",
        "AI generated video",
    ]

    extra_keywords = [
        w.strip().lower()
        for w in title.split()
        if len(w) > 3  # skip tiny words like "a", "the", "of"
    ]

    # Remove duplicates but keep order
    keywords: List[str] = list(dict.fromkeys(base_keywords + extra_keywords))

    # Tags: similar to keywords but in tag-style
    tags: List[str] = [kw.replace(" ", "-") for kw in keywords][:15]

    cta = "Subscribe for more AI-powered story videos every week!"

    return {
        "description": description,
        "keywords": keywords,
        "tags": tags,
        "cta": cta,
    }


if __name__ == "__main__":
    # Quick standalone test
    meta = generate_metadata(
        title="True Scary Story From A Nurse Working Night Shift",
        topic="a horror story from a hospital night shift",
        niche="horror stories",
        script="Once upon a night shift...",
    )
    print("DESCRIPTION:\n", meta["description"])
    print("\nTAGS:\n", ", ".join(meta["tags"]))
