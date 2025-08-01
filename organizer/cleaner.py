"""
Cleaning and normalization for transcripts and lessons.
"""

import re

def clean_transcript(text):
    """
    Clean transcript text:
      - Remove metadata table (everything before and including first blank line after '## Transcript')
      - Remove all '[mm:ss]' timestamp tokens
      - Collapse multiple blank lines
      - Keep only readable text/paragraphs
    Returns cleaned string.
    """
    lines = text.splitlines()
    body = []
    in_body = False
    found_transcript = False
    for i, line in enumerate(lines):
        if not found_transcript and line.strip().startswith("## Transcript"):
            found_transcript = True
        elif found_transcript and not in_body and line.strip() == "":
            in_body = True
            continue
        elif in_body:
            body = lines[i:]
            break
    if not body:
        # fallback: use all lines if parsing failed
        body = lines

    body_text = "\n".join(body)
    # Remove [mm:ss] tokens
    body_text = re.sub(r"\[\d{2}:\d{2}\]", "", body_text)
    # Collapse multiple blank lines
    body_text = re.sub(r"\n{3,}", "\n\n", body_text)
    return body_text.strip()

def clean_lesson(text):
    """
    Clean lesson text:
      - Strip leading/trailing whitespace
      - Collapse >2 consecutive blank lines to 2
    Returns cleaned string.
    """
    text = text.strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text