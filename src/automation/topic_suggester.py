from dataclasses import dataclass
from typing import List
import random

from dotenv import load_dotenv

# Optional: If you already have an LLM client in your project, we can call it.
# For now, we keep this module working even without any API key.
load_dotenv()


@dataclass
class TopicSuggestionResult:
    topics: List[str]
    source: str  # "fallback" or "llm"


# --- Fallback topic templates (works offline) ---
GENRE_TEMPLATES = {
    "horror": [
        "A night shift nurse hears a patient whisper her name—when no one is there",
        "A security camera shows a figure that never appears in the hallway",
        "The hospital room that is always locked suddenly has a call light on",
        "A patient is admitted… but their file doesn’t exist",
        "The elevator stops at a floor that isn’t on the buttons",
        "A voice comes from an empty ICU bed at 3:07 AM",
    ],
    "tech": [
        "What is {keyword}? Explained simply with real-life examples",
        "AI vs Machine Learning vs Deep Learning — what’s the difference?",
        "How does the Internet actually work? (No jargon)",
        "Top 5 beginner mistakes in {keyword} and how to avoid them",
        "The simplest explanation of {keyword} you’ll ever hear",
        "How {keyword} is used in real companies",
    ],
    "psychology": [
        "Why do we overthink at night? Psychology explained",
        "The psychology of fear: why our brain tricks us",
        "What is cognitive dissonance? Real examples",
        "How habits form in the brain (and how to change them)",
        "Why do people procrastinate? A psychological breakdown",
        "The science of motivation: what actually works",
    ],
    "motivational": [
        "How to stay disciplined when motivation is gone",
        "A short story about failure that changes your mindset",
        "Why consistency beats talent (with examples)",
        "How to rebuild your confidence after setbacks",
        "The mindset shift that makes success easier",
        "What successful people do when no one is watching",
    ],
    "educational": [
        "What is {keyword}? Explained for beginners",
        "How {keyword} works step-by-step",
        "The 5-minute guide to {keyword}",
        "Common myths about {keyword} (and the truth)",
        "A simple lesson on {keyword} with examples",
        "What students should know about {keyword}",
    ],
}


def _extract_keyword(topic_seed: str, genre: str) -> str:
    """Very simple keyword extraction. Works without NLP libraries."""
    seed = (topic_seed or "").strip()
    if not seed:
        # sensible defaults
        return "AI" if genre in ("tech", "educational") else "this topic"

    # pick a short keyword-ish phrase from the seed
    words = [w.strip("?,.!").strip() for w in seed.split() if w.strip()]
    if not words:
        return "AI"
    # keep it short
    return " ".join(words[:3])


def suggest_topics(
    genre: str,
    niche: str,
    tone: str,
    topic_seed: str = "",
    count: int = 8,
) -> TopicSuggestionResult:
    """
    Returns topic suggestions. Uses fallback templates (offline) for now.
    Later we can plug in LLM suggestions too.
    """
    genre_key = (genre or "educational").strip().lower()
    templates = GENRE_TEMPLATES.get(genre_key, GENRE_TEMPLATES["educational"])

    keyword = _extract_keyword(topic_seed or niche, genre_key)

    # expand templates with {keyword} where present
    expanded = []
    for t in templates:
        expanded.append(t.format(keyword=keyword))

    random.shuffle(expanded)

    # If count > available, cycle
    topics = []
    i = 0
    while len(topics) < count:
        topics.append(expanded[i % len(expanded)])
        i += 1

    # Light tone adjustment (simple)
    if tone == "casual":
        topics = [t.replace("Explained", "Explained (simple)").replace("step-by-step", "step by step") for t in topics]
    elif tone == "dramatic":
        topics = [t + " (with a twist)" if genre_key == "horror" and "(with a twist)" not in t else t for t in topics]

    return TopicSuggestionResult(topics=topics, source="fallback")
