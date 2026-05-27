"""
Local script generator for YouTube videos (no external API).

Supports multiple genres:
- horror
- motivational
- tech
- psychology
- educational

Each call returns:
- title
- outline
- full_script
"""

import random
from typing import Dict


# ---------------- HORROR -----------------

def _normalize_tone(tone: str) -> str:
    t = tone.strip().lower()
    if t in {"story", "storytelling"}:
        return "storytelling"
    if t in {"casual", "chill"}:
        return "casual"
    if t in {"dramatic", "intense"}:
        return "dramatic"
    return "storytelling"

def _generate_random_horror_story(topic: str, target_duration_minutes: int) -> Dict[str, str]:
    settings = [
        "an old hospital during the night shift",
        "a remote village clinic with no electricity",
        "a nearly empty city hospital during a storm",
        "a small-town ER where strange things always happen",
    ]

    entities = [
        "a patient who was never admitted",
        "a nurse who disappeared years ago",
        "a child only seen on the security cameras",
        "a shadowy figure standing at the end of the hallway",
    ]

    noises = [
        "the sound of footsteps in an empty corridor",
        "a monitor beeping in a room with no patient",
        "whispers coming from the supply closet",
        "the elevator opening on a floor that is closed at night",
    ]

    twists = [
        "the nurse realizes the calls are coming from a room that was demolished years ago",
        "the security footage shows the nurse talking to no one",
        "the patient file she’s been holding all night belongs to herself",
        "the night shift she is working never actually ended",
    ]

    setting = random.choice(settings)
    entity = random.choice(entities)
    noise = random.choice(noises)
    twist = random.choice(twists)

    approx_words = target_duration_minutes * 130

    title = random.choice(
        [
            "The Night Shift No One Talks About",
            "The Patient Who Wasn't There",
            "What the Cameras Saw at 3 A.M.",
            "The Call from Room 12",
        ]
    )

    outline = (
        "1. Introduction to the night shift and setting\n"
        "2. Strange events begin\n"
        "3. Tension builds as the nurse investigates\n"
        "4. Final twist and reflection\n"
    )

    intro = (
        f"It was just after 2 A.M. when the hospital finally went quiet. "
        f"Only the dim emergency lights were on, and {topic.lower()} felt like just another long night. "
        f"The nurse on duty was exhausted, but something about this shift felt different. "
        f"The hospital, {setting}, seemed to be holding its breath.\n\n"
    )

    middle = (
        f"Things started small. First, there was {noise}. "
        f"At first, the nurse tried to ignore it, telling herself it was just a machine resetting or a door not fully closed. "
        f"But then she noticed something else: {entity}. "
        f"Other staff members had gone home hours ago, yet she kept seeing movement at the end of the hallway—"
        f"a figure turning the corner just as she looked up.\n\n"
        f"When she checked the rooms, they were always empty. "
        f"The computers showed no new admissions. "
        f"Still, call lights flickered on in rooms that were supposed to be locked, "
        f"and the intercom crackled with faint voices asking for help.\n\n"
    )

    build_up = (
        "As the night went on, the events grew more intense. "
        "Monitors displayed vital signs for patients who weren't there. "
        "A wheelchair rolled slowly down the hallway on its own, stopping right in front of her. "
        "The nurse tried to stay logical—maybe a draft, maybe a glitch—but her hands were shaking.\n\n"
        "She finally decided to check the security office. "
        "If anything strange was happening, it would be on the cameras.\n\n"
    )

    twist_paragraph = (
        f"When she rewound the footage, her heart dropped. "
        f"On the screen, she saw herself walking down the hall, pausing at doors, checking rooms—"
        f"but the {entity} she remembered talking to was never there. "
        f"In one clip, she watched herself stand in the middle of the hallway, speaking softly to thin air.\n\n"
        f"And then came the final clip: the time stamp showed the current time. "
        f"In the live feed, she watched herself staring at the cameras in horror. "
        f"Behind her, in the video, {twist}.\n\n"
    )

    conclusion = (
        "The next morning, the nurse tried to explain what happened, but no one believed her. "
        "The reports mentioned a busy but otherwise normal night. "
        "Yet she knew what she heard, what she saw, and how cold the hallway felt.\n\n"
        "From that night on, she never worked the night shift alone again. "
        "And somewhere in that hospital, the cameras are still recording—"
        "waiting for the next person who stays too late.\n\n"
        f"(Approximate target length: ~{approx_words} words of narration.)"
    )

    full_script = intro + middle + build_up + twist_paragraph + conclusion

    return {
        "title": f"{title} – A {topic.title()}",
        "outline": outline,
        "full_script": full_script,
    }


# --------------- MOTIVATIONAL ---------------


def _generate_motivational_story(topic: str, target_duration_minutes: int) -> Dict[str, str]:
    journeys = [
        "an international student moving to a new country",
        "someone failing their exams multiple times",
        "a first-generation college student working night shifts",
        "someone who felt completely lost in their 20s",
    ]

    obstacles = [
        "language barriers and cultural shock",
        "rejections from internships and job applications",
        "financial pressure and family expectations",
        "self-doubt and anxiety about the future",
    ]

    turning_points = [
        "decides to treat every failure as feedback",
        "meets a mentor who changes their perspective",
        "starts building tiny daily habits instead of big plans",
        "realizes they don’t need to be perfect to make progress",
    ]

    lessons = [
        "progress is often invisible until you look back",
        "discipline beats motivation when things get hard",
        "your background is not a limitation but a unique strength",
        "no one is coming to save you—but you are capable of saving yourself",
    ]

    journey = random.choice(journeys)
    obstacle = random.choice(obstacles)
    turning_point = random.choice(turning_points)
    lesson = random.choice(lessons)

    approx_words = target_duration_minutes * 130

    title = random.choice(
        [
            "From Rock Bottom to Restart",
            "The Day I Stopped Waiting for Motivation",
            "How One Decision Changed Everything",
            "You Are Closer Than You Think",
        ]
    )

    outline = (
        "1. Relatable opening and context\n"
        "2. Main struggle and challenges\n"
        "3. Turning point and new mindset\n"
        "4. Outcomes and key lessons\n"
    )

    intro = (
        f"Everyone sees the success posts, the graduation photos, the new job announcements. "
        f"But almost no one talks honestly about the messy middle. "
        f"This is a story about {journey}, and how they turned {topic.lower()} into a real turning point.\n\n"
    )

    middle = (
        f"At first, everything felt exciting. New environment, new chances, new goals. "
        f"But reality hit hard: {obstacle}. "
        f"The more they tried to fix everything at once, the more overwhelmed they felt.\n\n"
        "They compared themselves to others constantly. "
        "Every time they scrolled social media, it seemed like everyone else was ahead—better grades, better jobs, better lives. "
        "Slowly, they began to believe they just weren't good enough.\n\n"
    )

    turn = (
        f"The turning point came when they {turning_point}. "
        "Instead of trying to change everything overnight, they picked one small action and repeated it daily. "
        "One extra hour of focused study. One email to a potential mentor. One consistent habit, even on bad days.\n\n"
        "Days turned into weeks. Weeks into months. "
        "There was no dramatic movie scene, no sudden miracle. "
        "Just quiet, steady improvement that only became visible over time.\n\n"
    )

    conclusion = (
        f"In the end, their life didn’t become perfect—but it became theirs. "
        f"They learned that {lesson}. "
        "If you’re going through something similar, remember: you don’t have to feel ready to start. "
        "You just have to be willing to move one step forward today.\n\n"
        f"(Approximate target length: ~{approx_words} words of narration.)"
    )

    full_script = intro + middle + turn + conclusion

    return {
        "title": f"{title} – A Story About {topic.title()}",
        "outline": outline,
        "full_script": full_script,
    }


# --------------- TECH EXPLAINER ---------------


def _generate_tech_explainer(topic: str, target_duration_minutes: int, tone: str) -> Dict[str, str]:
    topic_lower = topic.lower()
    tone_norm = _normalize_tone(tone)
    approx_words = target_duration_minutes * 130

    # Tone styling
    if tone_norm == "casual":
        intro_style = "Alright, let’s break this down in the simplest way possible."
        vibe = "Think of it like explaining something to a friend at a café."
    elif tone_norm == "dramatic":
        intro_style = "What if I told you the technology shaping the world is far simpler than you think?"
        vibe = "Let’s uncover it like a movie reveal."
    else:  # storytelling
        intro_style = "In this video, we’ll break down the topic step by step."
        vibe = "No fluff, just clarity."

    # Detect specific tech topics
    if "ai" in topic_lower or "artificial intelligence" in topic_lower:
        subject = "Artificial Intelligence"
        definition = (
            "Artificial Intelligence, or AI, is a field of computer science where machines are designed "
            "to mimic human intelligence—like learning, reasoning, problem-solving, or recognizing patterns."
        )
        how_it_works = (
            "AI works by taking data, learning from that data through models, "
            "and then making predictions or decisions. For example:\n"
            "- YouTube recommending videos\n"
            "- Google Maps predicting traffic\n"
            "- Chatbots answering questions\n"
        )
        real_world = (
            "AI is behind facial recognition, voice assistants, banking fraud detection, and even self-driving cars."
        )
    elif "machine learning" in topic_lower:
        subject = "Machine Learning"
        definition = (
            "Machine learning is a branch of AI where computers learn patterns from data "
            "instead of being given step-by-step instructions."
        )
        how_it_works = (
            "You feed the algorithm lots of labeled examples, it adjusts its internal parameters, "
            "and over time it gets better at making predictions—like recognizing spam emails or handwritten digits."
        )
        real_world = "Machine learning powers spam filters, recommendation systems, and many classification tasks."
    elif "deep learning" in topic_lower:
        subject = "Deep Learning"
        definition = (
            "Deep learning is a type of machine learning that uses multi-layered neural networks "
            "to learn very complex patterns."
        )
        how_it_works = (
            "Data is passed through many layers. Each layer detects slightly more complex features "
            "until the network can recognize things like faces, voices, or objects."
        )
        real_world = "Deep learning is used in image recognition, voice assistants, and self-driving cars."
    else:
        # Generic fallback for any other tech topic
        subject = topic.title()
        definition = (
            f"{subject} is an important concept in technology, but many people misunderstand what it really means."
        )
        how_it_works = (
            "At a high level, here’s how it works:\n"
            "- You start with input data.\n"
            "- Apply rules, algorithms, or models.\n"
            "- Produce an output that is useful, predictive, or actionable.\n"
        )
        real_world = (
            "You interact with this technology every day—on your phone, computer, smart devices, and online accounts."
        )

    title = f"{subject} Explained Simply"

    outline = (
        "1. Hook & topic introduction\n"
        f"2. What {subject} means\n"
        f"3. How {subject} works\n"
        f"4. Real-world examples\n"
        "5. Final summary\n"
    )

    intro = (
        f"{intro_style} Today we’re talking about **{subject}**. {vibe}\n\n"
        f"So, what exactly is **{subject}**?"
    )

    explanation = (
        f"\n\n### What it means\n{definition}\n\n"
        f"### How it works\n{how_it_works}\n\n"
        f"### Real-world examples\n{real_world}\n\n"
    )

    conclusion = (
        f"In simple terms, **{subject}** helps computers understand the world and make useful decisions. "
        f"If you understand the basics, you're already ahead of most people.\n\n"
        f"(Approx. {approx_words} words of narration.)"
    )

    full_script = intro + explanation + conclusion

    return {
        "title": title,
        "outline": outline,
        "full_script": full_script,
    }



# --------------- PSYCHOLOGY ---------------


def _generate_psychology_story(topic: str, target_duration_minutes: int) -> Dict[str, str]:
    approx_words = target_duration_minutes * 130

    phenomena = [
        "confirmation bias",
        "impostor syndrome",
        "social anxiety",
        "the spotlight effect",
        "cognitive dissonance",
    ]

    examples = [
        "a student who feels like a fraud despite good grades",
        "someone who thinks everyone is judging them when they enter a room",
        "a person who stays in an unhealthy situation because change feels uncomfortable",
    ]

    phenomenon = random.choice(phenomena)
    example = random.choice(examples)

    title = random.choice(
        [
            "Why Our Brains Trick Us",
            "The Psychology Behind Your Everyday Thoughts",
            "You’re Not Weird, You’re Human",
        ]
    )

    outline = (
        "1. Relatable example\n"
        "2. Psychological concept explained\n"
        "3. How it shows up in daily life\n"
        "4. Simple strategies to cope\n"
    )

    intro = (
        f"Have you ever wondered why your brain reacts a certain way, even when you logically know better? "
        f"Today, we’ll talk about {phenomenon}, using {topic.lower()} as a starting point.\n\n"
    )

    explanation = (
        f"Imagine {example}. "
        "From the outside, it might seem irrational—but from the inside, it feels completely real. "
        f"This is where {phenomenon} comes in.\n\n"
    )

    life = (
        "In daily life, this can look like:\n"
        "- Overthinking what others think about you\n"
        "- Ignoring evidence that doesn’t match your beliefs\n"
        "- Feeling like you don’t belong, even when you’re doing fine\n\n"
    )

    strategies = (
        "A few simple strategies can help:\n"
        "- Notice the thought and label it instead of believing it automatically\n"
        "- Ask: 'What evidence do I have for and against this belief?'\n"
        "- Talk to someone you trust or a mental health professional when it feels heavy\n\n"
    )

    conclusion = (
        "The takeaway is this: your brain is not broken—it’s human. "
        "Understanding the psychology behind your reactions can take away some of the shame and confusion. "
        "You don’t have to fight every thought, but you can learn to respond to them differently.\n\n"
        f"(Approximate target length: ~{approx_words} words of narration.)"
    )

    full_script = intro + explanation + life + strategies + conclusion

    return {
        "title": f"{title} – Through the Lens of {topic.title()}",
        "outline": outline,
        "full_script": full_script,
    }


# --------------- EDUCATIONAL ---------------


def _generate_educational_script(topic: str, target_duration_minutes: int, tone: str) -> Dict[str, str]:
    tone_norm = _normalize_tone(tone)
    approx_words = target_duration_minutes * 130

    if tone_norm == "casual":
        intro = (
            f"Let’s talk about **{topic}** in the simplest way possible. "
            "No confusing textbook language—just the main idea.\n\n"
        )
    elif tone_norm == "dramatic":
        intro = (
            f"Behind many exams, lectures, and big decisions, there’s one key idea: **{topic}**. "
            "Today, we strip it down to what actually matters.\n\n"
        )
    else:  # storytelling / default
        intro = (
            f"In this short lesson, we’ll break down **{topic}** into simple, memorable pieces "
            "so you can review it quickly.\n\n"
        )

    body = (
        "### 1. Basic idea\n"
        f"Start by asking: *What is {topic} in one or two sentences?* "
        "If you can answer that, the rest becomes easier.\n\n"
        "### 2. Key points\n"
        "- Write down 3–5 bullet points that describe the most important facts.\n"
        "- Focus on big ideas, not tiny details.\n\n"
        "### 3. How it connects\n"
        f"Think about where **{topic}** shows up in real life—"
        "in news, technology, health, history, or everyday decisions.\n\n"
    )

    summary = (
        "### 4. Quick review trick\n"
        "Pause the video and try to explain this topic in your own words, "
        "as if you’re teaching a friend. If you can do that, you’ve already learned more than most people "
        "who just read it once.\n\n"
        f"(Approx. {approx_words} words of narration.)"
    )

    full_script = intro + body + summary

    return {
        "title": f"{topic.title()} – Explained Simply",
        "outline": "1. Basic idea\n2. Key points\n3. Connections\n4. Review",
        "full_script": full_script,
    }



# --------------- PUBLIC INTERFACE ---------------


def generate_script(
    topic: str,
    tone: str = "storytelling",
    target_duration_minutes: int = 8,
    genre: str = "horror",
) -> Dict[str, str]:
    """
    Main function used by the rest of the app.

    genre options:
    - "horror"
    - "motivational"
    - "tech"
    - "psychology"
    - "educational"
    """

    genre_normalized = genre.strip().lower()

    if genre_normalized == "horror":
        return _generate_random_horror_story(topic, target_duration_minutes)
    if genre_normalized == "motivational":
        return _generate_motivational_story(topic, target_duration_minutes)
    if genre_normalized == "tech":
        return _generate_tech_explainer(topic, target_duration_minutes, tone)
    if genre_normalized == "psychology":
        return _generate_psychology_story(topic, target_duration_minutes)
    if genre_normalized == "educational":
        return _generate_educational_script(topic, target_duration_minutes, tone)

    # default fallback
    return _generate_random_horror_story(topic, target_duration_minutes)


if __name__ == "__main__":
    result = generate_script(
        topic="true scary story from a nurse working night shift",
        tone="storytelling",
        target_duration_minutes=8,
        genre="horror",
    )
    print("\n--- TITLE ---\n", result["title"])
    print("\n--- OUTLINE ---\n", result["outline"])
    print("\n--- SCRIPT (first 400 chars) ---\n", result["full_script"][:400], "...")
