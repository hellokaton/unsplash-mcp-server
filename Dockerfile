FROM python:3.11-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN pip install --no-cache-dir uv

# Copy application code
COPY pyproject.toml uv.lock ./
COPY server.py ./

# install deps by uv
RUN uv pip install --system -r pyproject.toml

# Command will be provided by smithery.yaml
CMD ["python", "server.py"]