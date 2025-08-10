#!/usr/bin/env python3
import os
import re
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/workspace")
SOURCE_EXTS = {".md", ".txt"}
OUTPUT_DIR = WORKSPACE / "notes"
TEMPLATE_PATH = WORKSPACE / "templates" / "transcript_note_template.md"

META_PATTERNS = {
    "title": re.compile(r"^#\s+(.+)$", re.MULTILINE),
    "meta_title": re.compile(r"^-\s+\*\*Title:\*\*\s*(.+)$", re.MULTILINE),
    "author": re.compile(r"^-\s+\*\*Author:\*\*\s*(.+)$", re.MULTILINE),
    "source": re.compile(r"\*\*Source:\*\*\s*(.+)$", re.MULTILINE),
    "meta_duration": re.compile(r"^-\s+\*\*Duration:\*\*\s*([0-9]{1,2}:[0-9]{2})\b", re.MULTILINE),
    "meta_video_url": re.compile(r"^-\s+\*\*Video URL:\*\*\s*(https?://\S+)", re.MULTILINE),
    "any_url": re.compile(r"https?://\S+"),
}


def load_template() -> str:
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def extract_metadata(content: str, fallback_name: str) -> dict:
    # Prefer explicit metadata if present, else fall back
    title_match = META_PATTERNS["title"].search(content) or META_PATTERNS["meta_title"].search(content)
    title = title_match.group(1).strip() if title_match else fallback_name

    source_match = META_PATTERNS["source"].search(content)
    source = source_match.group(1).strip() if source_match else title

    mvurl = META_PATTERNS["meta_video_url"].search(content)
    anyurl = META_PATTERNS["any_url"].search(content)
    link = (mvurl.group(1) if mvurl else (anyurl.group(0) if anyurl else ""))

    # Duration heuristics: prefer explicit metadata, else parse minute markers
    dmeta = META_PATTERNS["meta_duration"].search(content)
    if dmeta:
        duration = dmeta.group(1)
    else:
        minute_markers = re.findall(r"\[(\d{2}:\d{2})]", content[:10000])
        duration = minute_markers[-1] if minute_markers else ""

    return {
        "title": title,
        "source": source,
        "link": link,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "duration": duration,
    }


def derive_time_outline(content: str) -> list:
    # Accept formats like: [00:00] text or lines starting with 00:00
    outline = []
    for line in content.splitlines():
        m = re.match(r"^\s*(?:\[(\d{2}:\d{2})]|(\d{2}:\d{2}))\s*[-–:]?\s*(.*)$", line)
        if m:
            ts = m.group(1) or m.group(2)
            txt = m.group(3).strip()
            if ts and txt:
                outline.append((ts, txt))
    # Deduplicate sequential identical timestamps
    dedup = []
    seen = set()
    for ts, txt in outline:
        key = (ts, txt)
        if key not in seen:
            dedup.append((ts, txt))
            seen.add(key)
    return dedup[:50]


def synthesize_tldr(content: str) -> str:
    # Simple heuristic TL;DR: first sentence trimmed
    first_para = next((p for p in content.strip().split("\n\n") if p.strip()), "")
    sentence = re.split(r"(?<=[.!?])\s+", first_para.strip())
    return sentence[0][:240] if sentence else ""


def build_note(template: str, meta: dict, outline: list, raw_path: Path) -> str:
    note = template
    def repl(marker: str, value: str) -> None:
        nonlocal note
        note = note.replace(marker, value)

    repl("Note Title", meta["title"])  # header line
    note = note.replace("<file or video name>", meta["source"])\
               .replace("<url if applicable>", meta["link"])\
               .replace("<YYYY-MM-DD>", meta["date"])\
               .replace("<HH:MM or minutes>", meta["duration"])\
               .replace("<name>", "")\
               .replace("<comma,separated,tags>", "transcript, notes")

    # TL;DR
    tldr = synthesize_tldr(Path(raw_path).read_text(encoding="utf-8"))
    note = note.replace("- One-sentence summary of the transcript.", f"- {tldr}" if tldr else "- TODO")

    # Outline
    if outline:
        outline_md = "\n".join([f"- {ts} – {txt}" for ts, txt in outline])
        note = re.sub(r"## Outline by Time\n[\s\S]*?\n\n## ", f"## Outline by Time\n\n{outline_md}\n\n## ", note)
    else:
        # leave template outline as-is
        pass

    # Raw reference path
    note = note.replace("<optional: paste or reference path>", str(raw_path))

    return note


def discover_sources() -> list[Path]:
    paths = []
    for p in WORKSPACE.iterdir():
        if p.is_file() and p.suffix.lower() in SOURCE_EXTS:
            # Skip already generated notes and template
            if p.parent.name == "notes":
                continue
            if p.name == TEMPLATE_PATH.name:
                continue
            paths.append(p)
    return paths


def sanitize_filename(name: str) -> str:
    # Normalize common YouTube/ID-like stems to keep meaningful IDs
    name = name.replace(" ", "-")
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name.strip())
    name = re.sub(r"-+", "-", name)
    return name.strip("-")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    template = load_template()

    for src in discover_sources():
        content = src.read_text(encoding="utf-8", errors="ignore")
        meta = extract_metadata(content, fallback_name=src.stem)
        outline = derive_time_outline(content)

        base_name = sanitize_filename(meta["title"]) or sanitize_filename(src.stem)
        out_path = OUTPUT_DIR / f"{base_name}.md"
        # Avoid collisions: if file exists, append source stem
        if out_path.exists():
            suffix = sanitize_filename(src.stem)
            out_path = OUTPUT_DIR / f"{base_name}__{suffix}.md"

        note = build_note(template, meta, outline, src)
        out_path.write_text(note, encoding="utf-8")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()