# Step 6: Push to GitHub — push_to_github

## What this step implements

Adds `push_to_github(filename)`, which compiles every saved entry into a
formatted markdown file and pushes it to a GitHub repo via the GitHub API.

## File structure

- `server.py` — all tools + resource + prompt + push_to_github
- `pyproject.toml` — now includes requests, python-dotenv
- `uv.lock`
- `.python-version`
- `.gitignore`
- `.env.example` — template for your token/repo
- `config/claude_desktop_config.json`

## Setup

**macOS / Linux / Windows** (same commands, `uv` handles the platform difference):
```bash
uv sync
```

Create a real `.env` file (never commit this) based on `.env.example`:
```
GITHUB_TOKEN=your_classic_personal_access_token
GITHUB_REPO=yourusername/your-content-repo
```

Generate a token at https://github.com/settings/tokens →
**Generate new token (classic)** → check the **repo** scope → generate.

Fully quit and reopen Claude Desktop so it picks up the new `.env`, then ask
it to push your learnings to GitHub.