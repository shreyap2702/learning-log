# Step 4: Prompt — summarize_week

## What this step implements

Adds a prompt template, `summarize_week`, a reusable, user-selected
instruction (not something the model calls on its own like a tool). This
completes all three MCP primitives: tools, resource, and prompt.

## File structure

- `server.py` — tools + resource + summarize_week prompt
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
In the Inspector, click the **Prompts** tab, select `summarize_week`, and
confirm it returns the summary instruction text.