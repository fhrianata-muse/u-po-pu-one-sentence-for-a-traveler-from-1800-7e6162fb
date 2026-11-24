#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — entry program.

Writes one sentence (an explanation of the modern internet for a person
from 1800) to /output/entry.txt. The sentence is kept as data; before
writing, the program re-checks the competition gate itself: plain text,
one sentence, 1 to 200 characters, not only white space, no leading or
trailing space, ending on terminal punctuation so the sentence reads
complete.
"""

import sys
from pathlib import Path

ENTRY = "It is a library where every book answers back when you ask it a question, and any man may speak with a stranger across the sea from his own chair."

# Words coined after 1800, which the brief forbids in the sentence.
BANNED = (
    "internet", "online", "digital", "screen", "phone", "photograph",
    "film", "video", "radio", "telegraph", "computer", "website", "email",
)

OUT = Path("/output/entry.txt")


def check(text):
    """Return a reason the text fails the gate, or None when it passes."""
    if "\n" in text or "\r" in text:
        return "entry must be a single sentence"
    if not 1 <= len(text) <= 200:
        return "entry must be 1 to 200 characters, got %d" % len(text)
    if not text.strip():
        return "entry must not be only white space"
    if text != text.strip():
        return "entry must not start or end with white space"
    if any(ord(ch) < 32 for ch in text):
        return "entry must not contain control characters"
    if "  " in text:
        return "entry must not contain double spaces"
    lowered = text.lower()
    for word in BANNED:
        if word in lowered:
            return "entry must not use a word coined after 1800: %s" % word
    if text[-1] not in ".!?":
        return "entry must end with terminal punctuation"
    return None


def main():
    problem = check(ENTRY)
    if problem is not None:
        print("gate failed: " + problem, file=sys.stderr)
        raise SystemExit(1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
