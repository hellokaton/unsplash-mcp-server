# Unsplash MCP Server

A MCP server for Unsplash image search and utilities.

## Features

- **Image Search**: Search Unsplash photos with various filters

## Prerequisites

- Python 3.9+
- UV package manager (`pip install uv`)
- Unsplash Access Key (register at [Unsplash Developers](https://unsplash.com/developers))

## Installation

```bash
git clone https://github.com/hellokaton/unsplash-mcp-server.git
cd unsplash-mcp-server
uv venv  # Create virtual environment
uv pip install -r requirements.txt  # Install dependencies
```

## Usage

### Local Development

Create a `.env` file:

```env
UNSPLASH_ACCESS_KEY=your_access_key_here
```

For local testing and development:

```bash
fastmcp dev server.py
```

### Cursor Integration

To use with Cursor editor, add this configuration to your settings.json:

```json
{
  "mcpServers": {
    "unsplash": {
      "command": "uv",
      "args": ["run", "--with", "fastmcp", "fastmcp", "run", "./server.py"],
      "env": {
        "UNSPLASH_ACCESS_KEY": "${YOUR_ACCESS_KEY}"
      }
    }
  }
}
```

### Cursor Usage

> I am preparing a screenshot for using the cursor, but it has crashed and I need to add it later.

## Available Tools

### Search Photos

```json
{
  "tool": "search_photos",
  "query": "mountain",
  "per_page": 5,
  "orientation": "landscape"
}
```

## License

[MIT](LICENSE) License

## Contact

- [X/Twitter](https://x.com/hellokaton)
