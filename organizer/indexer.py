"""
Index builder for cleaned files.
"""

import json
from pathlib import Path
from organizer.utils import get_top_keywords, slugify

def build_index(clean_root):
    """
    Scan cleaned/transcripts and cleaned/lessons, build index.json at clean_root.
    Each record: {
        "title": ...,
        "slug": ...,
        "category": "transcript|lesson",
        "orig_path": ...,
        "clean_path": ...,
        "keywords": [...],
        "summary": ...
    }
    """
    clean_root = Path(clean_root)
    out = []
    for category in ["transcripts", "lessons"]:
        cat_dir = clean_root / category
        if not cat_dir.exists():
            continue
        for file in cat_dir.glob("*.md"):
            try:
                with open(file, encoding="utf-8") as f:
                    text = f.read()
                # Try to find original path in file metadata (if we want), else guess
                title = file.stem.replace("-", " ").title()
                summary = " ".join(text.split()[:30])
                keywords = get_top_keywords(text)
                rec = {
                    "title": title,
                    "slug": file.stem,
                    "category": category[:-1],
                    "orig_path": None,  # filled in by CLI
                    "clean_path": str(file.relative_to(clean_root.parent)),
                    "keywords": keywords,
                    "summary": summary
                }
                out.append(rec)
            except Exception:
                continue
    # Fill orig_path where possible by matching slugs
    orig_map = {}
    for p in Path(".").glob("*.md"):
        orig_map[slugify(p.stem)] = str(p)
    for p in Path(".").glob("*.txt"):
        orig_map[slugify(p.stem)] = str(p)
    for rec in out:
        slug = rec["slug"]
        if slug in orig_map:
            rec["orig_path"] = orig_map[slug]
    # Write index
    index_path = clean_root / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)