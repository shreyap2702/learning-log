import base64
import json
import os
from datetime import datetime
from typing import Annotated

import requests
from dotenv import load_dotenv
from pydantic import Field
from mcp.server import MCPServer

load_dotenv()

mcp = MCPServer("learning-log")
DATA_FILE = os.path.join(os.path.dirname(__file__), "learnings.json")

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPO")


def _load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def _save(entries):
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=2)


@mcp.tool()
def add_learning(
    topic: Annotated[str, Field(description="Short title for the entry, e.g. 'MCP tools vs resources'")],
    details: Annotated[str, Field(description="A thorough, multi-sentence explanation of what was learned, written so someone with no context could understand the concept just from reading this")],
) -> str:
    """Save a new learning entry. Call this whenever the user shares something
    they learned during the conversation, even multiple times across a long chat.
    Write 'details' as a real, thorough explanation, several sentences covering
    what the concept is, how it works, and why it matters, not a short tag or summary."""
    entries = _load()
    entries.append({
        "topic": topic,
        "details": details,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    _save(entries)
    return f"Saved: {topic}"


@mcp.tool()
def search_learnings(
    keyword: Annotated[str, Field(description="Word to search for in saved topics or details")],
) -> str:
    """Search saved learnings for a keyword in the topic or details."""
    entries = _load()
    matches = [
        e for e in entries
        if keyword.lower() in e["topic"].lower() or keyword.lower() in e["details"].lower()
    ]
    if not matches:
        return f"No learnings found for '{keyword}'"
    return "\n\n".join(f"[{e['date']}] {e['topic']}\n{e['details']}" for e in matches)


@mcp.resource("learnings://all")
def all_learnings() -> str:
    """Expose every saved learning entry as raw JSON data."""
    entries = _load()
    return json.dumps(entries, indent=2)


@mcp.prompt()
def summarize_week() -> str:
    """Reusable prompt template to summarize this week's learnings."""
    return (
        "Look at all my logged learnings and give me a short summary of what "
        "I learned this week, grouped by topic."
    )


def _build_markdown(entries):
    lines = ["# My Learning Log", ""]
    for e in entries:
        lines.append(f"## {e['topic']}")
        lines.append(f"*{e['date']}*")
        lines.append("")
        lines.append(e["details"])
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def push_to_github(
    filename: Annotated[str, Field(description="Name of the markdown file to create or update in the repo, e.g. 'learnings.md'")] = "learnings.md",
) -> str:
    """Push all logged learnings to a formatted markdown file in the configured GitHub repo."""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        return "GitHub is not configured. Set GITHUB_TOKEN and GITHUB_REPO in your .env file."

    entries = _load()
    if not entries:
        return "No learnings to push yet."

    content = _build_markdown(entries)
    encoded = base64.b64encode(content.encode()).decode()

    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{filename}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }

    existing = requests.get(url, headers=headers)
    sha = existing.json().get("sha") if existing.status_code == 200 else None

    payload = {"message": f"update {filename}", "content": encoded}
    if sha:
        payload["sha"] = sha

    resp = requests.put(url, headers=headers, json=payload)
    if resp.status_code in (200, 201):
        return f"Pushed to {GITHUB_REPO}/{filename}"
    return f"Failed ({resp.status_code}): {resp.text}"


if __name__ == "__main__":
    mcp.run()