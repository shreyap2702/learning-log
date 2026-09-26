# Step 0: Setup

## What this step implements

Nothing yet, just the project scaffold and dependencies. No server code.

## File structure

- `pyproject.toml` — declares the mcp[cli] dependency
- `uv.lock` — locked dependency versions
- `.python-version` — pinned Python version
- `.gitignore`

## Setup

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init mcp-learning-log
cd mcp-learning-log
uv venv
uv add "mcp[cli]"
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv init mcp-learning-log
cd mcp-learning-log
uv venv
uv add "mcp[cli]"
```

Verify it installed correctly:
```bash
uv run python3 -c "import mcp; print('ok')"
```