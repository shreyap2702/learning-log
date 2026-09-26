# Step 3: Resource — learnings://all

## What this step implements

Adds a resource, `learnings://all`, that exposes every saved entry as raw
JSON. Unlike a tool, a resource is read-only data the client fetches, not
an action the model calls.

## File structure

- `server.py` — add_learning + search_learnings + learnings://all
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
In the Inspector, click the **Resources** tab, select `learnings://all`,
and confirm it returns a JSON array of your saved entries.