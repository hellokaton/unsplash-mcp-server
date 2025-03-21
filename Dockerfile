# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
FROM python:3.11-alpine

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

WORKDIR /app

# Copy project files
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir .

# Expose any necessary port if needed, for example 8000
# EXPOSE 8000

# Run the MCP server
CMD ["fastmcp", "run", "server.py"]
