# Step 2: Second tool — search_learnings

## What this step implements

Adds `search_learnings(keyword)`, which searches saved entries by topic or
details and returns matches, alongside `add_learning` from step 1.

## File structure

- `server.py` — add_learning + search_learnings
- `pyproject.toml`
- `uv.lock`
- `.python-version`
- `.gitignore`

## Setup

Same on macOS, Linux, and Windows:
```bash
uv sync
uv run mcp dev server.py
```
Add a couple of entries with `add_learning`, then call `search_learnings`
with a keyword that should match, and one that shouldn't.