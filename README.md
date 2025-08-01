# indycourse

---

## Repository Organizer

This repository includes a reusable Python CLI tool for organizing course assets.

### What it Does

- Scans the repo root for all `.md` and `.txt` files (excluding `/cleaned`)
- Classifies each as a **transcript** (YouTube transcript) or **lesson** (curated course material)
- Cleans and normalizes content (removes transcript timestamps/metadata, trims/normalizes lessons)
- Creates a `/cleaned/` directory:
  - `/cleaned/transcripts/` — cleaned transcript markdowns
  - `/cleaned/lessons/` — cleaned lesson markdowns
- Files are renamed with slugified, descriptive titles
- Builds a `/cleaned/index.json` for search/discovery (title, slug, category, original/cleaned paths, keywords, summary)
- Idempotent: safe to run repeatedly

### Usage

```bash
# One-shot organization
python organize_repo.py

# Rebuild from scratch (removes /cleaned/)
python organize_repo.py --rebuild
```

### Code Structure

- `organize_repo.py` — CLI entrypoint
- `organizer/`
    - `__init__.py`
    - `classifier.py` — file type/classification logic
    - `cleaner.py` — content cleaning utilities
    - `indexer.py` — index building for cleaned files
    - `utils.py` — slugification, stopwords, helpers
    - `tests/test_classifier.py` — basic file classification tests

### Example Test

```bash
python -m organizer.tests.test_classifier
```

---
