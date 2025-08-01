"""
Repository Organizer CLI
"""

import argparse
import os
import shutil
from pathlib import Path

from organizer.classifier import classify_file
from organizer.cleaner import clean_transcript, clean_lesson
from organizer.utils import slugify
from organizer.indexer import build_index

CLEAN_ROOT = Path("cleaned")
TRANS_DIR = CLEAN_ROOT / "transcripts"
LESSON_DIR = CLEAN_ROOT / "lessons"

def find_files():
    """Find all .md and .txt files in repo root, excluding /cleaned."""
    files = []
    for p in Path(".").iterdir():
        if p.is_file() and (p.suffix.lower() in [".md", ".txt"]):
            if "cleaned" not in str(p):
                files.append(p)
    return files

def main():
    parser = argparse.ArgumentParser(description="Repository Organizer CLI")
    parser.add_argument("--rebuild", action="store_true", help="Delete /cleaned then rebuild")
    args = parser.parse_args()

    if args.rebuild and CLEAN_ROOT.exists():
        shutil.rmtree(CLEAN_ROOT)

    TRANS_DIR.mkdir(parents=True, exist_ok=True)
    LESSON_DIR.mkdir(parents=True, exist_ok=True)

    files = find_files()
    filemap = {}

    for path in files:
        res = classify_file(path)
        if not res:
            continue
        category = res["category"]
        title = res["title"]
        slug = slugify(title)
        # Determine output path
        outdir = TRANS_DIR if category == "transcript" else LESSON_DIR
        outfile = outdir / f"{slug}.md"
        if outfile.exists():
            continue  # idempotency: skip if already cleaned
        # Read file, clean
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        cleaned = clean_transcript(raw) if category == "transcript" else clean_lesson(raw)
        # Write cleaned file
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(cleaned.strip() + "\n")
        filemap[slug] = {
            "title": title,
            "slug": slug,
            "category": category,
            "orig_path": str(path),
            "clean_path": str(outfile)
        }
    # Build index and patch in orig_path
    build_index(CLEAN_ROOT)
    # Patch index with improved orig_path if possible
    index_path = CLEAN_ROOT / "index.json"
    if index_path.exists():
        import json
        with open(index_path, encoding="utf-8") as f:
            data = json.load(f)
        for rec in data:
            slug = rec["slug"]
            if slug in filemap:
                rec["orig_path"] = filemap[slug]["orig_path"]
                rec["title"] = filemap[slug]["title"]
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    print("Repository organization complete.")

if __name__ == "__main__":
    main()