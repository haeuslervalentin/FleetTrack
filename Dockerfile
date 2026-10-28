FROM python:3.14-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock* ./

RUN uv sync --no-dev

COPY . .

EXPOSE 8000

CMD ["uv", "run", "python", "-m", "mcp_server.server"]
