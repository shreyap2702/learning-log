# Step 5: Connect to Claude Desktop

## What this step implements

No new server code. Adds an example Claude Desktop config so the server
can be launched and used directly from a real chat, not just the Inspector.

## File structure

- `server.py`
- `pyproject.toml`
- `uv.lock`
- `.python-version`
- `.gitignore`
- `config/claude_desktop_config.json` — example mcpServers entry

## Setup

1. Get your project's absolute path and your `uv` path:

   **macOS / Linux:**
   ```bash
   pwd
   which uv
   ```

   **Windows (PowerShell):**
   ```powershell
   (Get-Location).Path
   where.exe uv
   ```

2. Open Claude Desktop → **Settings → Developer → Edit Config**.

3. Add an `mcpServers` entry (keep anything already in the file):
   ```json
   {
     "mcpServers": {
       "learning-log": {
         "command": "/path/to/uv",
         "args": ["--directory", "/path/to/mcp-learning-log", "run", "server.py"]
       }
     }
   }
   ```
   On Windows, use double backslashes in paths, e.g. `"C:\\Users\\you\\mcp-learning-log"`.

4. Fully quit and reopen Claude Desktop. Check the connectors list for
   `learning-log`.