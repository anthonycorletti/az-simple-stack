FROM python:3.12.5-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN apt-get update -y \
  && rm -rf /var/lib/apt/lists/*

COPY . /api
WORKDIR /api

RUN uv sync --frozen

CMD ["uv", "run", "bin/run"]
