# FastAPI Boilerplate (uv + `pyproject.toml`)

Minimal FastAPI template with SQL + Mongo support, managed with [uv](https://docs.astral.sh/uv/).

## Structure

```
├── src/
│   └── app/
│       ├── api/          # routers (api/router.py, api/v1/...)
│       ├── core/         # settings (core/config.py)
│       ├── db/           # SQLAlchemy Base, engines, sessions
│       ├── models/       # ORM models
│       ├── schemas/      # Pydantic request/response schemas
│       ├── services/     # business logic
│       └── main.py       # app factory + instance
├── tests/
├── .github/workflows/   # CI (ruff, mypy, pytest)
├── pyproject.toml
├── uv.lock
├── Dockerfile
├── compose.yaml
└── README.md
```

Flow:

```
uvicorn app.main:app -> main.py -> api/router -> api/v1/* -> services <-> models/schemas
```

## Requirements

- Python from `.python-version` (3.12)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (replaces `pip` + `virtualenv` + `requirements.txt`)

## Setup

```bash
cp .env.example .env
uv sync            # creates .venv and installs locked deps (incl. dev group)
```

No manual `virtualenv` / `pip install -r requirements.txt` needed — `uv sync` handles it from `pyproject.toml` + `uv.lock`.

## Run

```bash
uv run uvicorn app.main:app --reload --app-dir src
```

Health check: `GET http://localhost:8000/healthcheck/` (also versioned at `/api/v1/healthcheck/`).

## Checks

```bash
uv run ruff check src tests
uv run ruff format --check src tests
uv run mypy src
uv run pytest
```

## Docker

```bash
docker build -t fastapi-boilerplate .
docker run -p 8000:8000 --env-file .env fastapi-boilerplate
# or
docker compose up --build
```

## Add a dependency

```bash
uv add <package>          # runtime dep -> pyproject.toml + uv.lock
uv add --group dev <pkg>  # dev-only dep
uv lock --upgrade         # refresh lockfile
```
