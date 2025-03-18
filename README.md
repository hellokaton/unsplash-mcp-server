# Unsplash MCP Server

> A simple MCP server for seamless Unsplash image integration and search capabilities.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![smithery badge](https://smithery.ai/badge/@hellokaton/unsplash-mcp-server)](https://smithery.ai/server/@hellokaton/unsplash-mcp-server)

## 📋 Overview

Unsplash MCP Server provides a simple yet powerful interface to search and utilize Unsplash's vast collection of high-quality images through MCP. Perfect for developers looking to integrate Unsplash functionality into their applications or Cursor editor workflows.

## ✨ Features

- **Advanced Image Search**: Search Unsplash's extensive photo library with filters for:
  - Keyword relevance
  - Color schemes
  - Orientation options
  - Custom sorting and pagination

## 🔧 Prerequisites

- Python 3.9 or higher
- UV package manager (`pip install uv`)
- Unsplash API Access Key (register at [Unsplash Developers Portal](https://unsplash.com/developers))

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/hellokaton/unsplash-mcp-server.git

# Navigate to project directory
cd unsplash-mcp-server

# Create virtual environment
uv venv

# Install dependencies
uv pip install .
```

## 💻 Usage

### Local Development

1. Create a `.env` file in the root directory:

```env
UNSPLASH_ACCESS_KEY=your_access_key_here
```

2. Run the server in development mode:

```bash
fastmcp dev server.py
```

### Cursor Editor Integration

Add the following configuration to your Cursor editor's `settings.json`:

⚠️ **Note:** Please adjust the following configuration according to your actual installation:

- If `uv` is not in your system PATH, use an absolute path (e.g., `/path/to/uv`)
- `./server.py` should be modified to the actual location of your server script (can use absolute path or path relative to workspace)

<img src="screenshots/Snipaste_1.png" alt="Cursor Configuration Screenshot" />

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

### Using in Cursor

<img src="screenshots/Snipaste_2.png" alt="Unsplash MCP in Cursor" />

## 🛠️ Available Tools

### Search Photos

```json
{
  "tool": "search_photos",
  "query": "mountain",
  "per_page": 5,
  "orientation": "landscape"
}
```

## 📄 License

[MIT License](LICENSE)

## 📬 Contact

- [Twitter/X](https://x.com/hellokaton)
- [GitHub Issues](https://github.com/hellokaton/unsplash-mcp-server/issues)
