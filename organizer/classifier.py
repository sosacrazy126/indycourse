"""
File classification utilities for the Repository Organizer.
"""

import re
from pathlib import Path

def classify_file(filepath):
    """
    Classify a file as 'transcript' or 'lesson' and extract a descriptive title.
    Heuristics:
      - transcript: "# YouTube Video Transcript" in first 30 lines, or any '[00:' timestamp
      - lesson: .txt ending in v4/v5, or lacking transcript markers
    Returns: dict with keys: category ('transcript'|'lesson'), title (string)
    """
    p = Path(filepath)
    category = None
    title = None

    # Ignore files inside /cleaned
    if "cleaned" in p.parts:
        return None

    ext = p.suffix.lower()
    is_txt = ext == ".txt"

    try:
        with open(filepath, encoding="utf-8") as f:
            lines = [next(f) for _ in range(30)]
    except StopIteration:
        with open(filepath, encoding="utf-8") as f:
            lines = list(f)

    lines = [l.rstrip('\n') for l in lines]
    first30 = "\n".join(lines)

    # Transcript heuristics
    if any("# YouTube Video Transcript" in l for l in lines):
        category = "transcript"
    elif re.search(r"\[\d{2}:\d{2}\]", first30):
        category = "transcript"

    # Lesson heuristics
    if not category:
        if is_txt and re.search(r"v[45](\.txt)?$", str(p.name)):
            category = "lesson"
        else:
            category = "lesson"

    # Title extraction
    if category == "transcript":
        # Find "Title: ..." in first 30 lines
        for l in lines:
            match = re.match(r"-\s*\*\*Title:\*\*\s*(.+)", l)
            if match:
                title = match.group(1).strip()
                break
        if not title:
            title = p.stem
    else:
        # Lesson: use first non-empty, non-marker line as title
        for l in lines:
            t = l.strip()
            if t and not t.startswith("#"):
                title = t.split(".")[0] if "." in t else t
                break
        if not title:
            title = p.stem

    return {"category": category, "title": title}