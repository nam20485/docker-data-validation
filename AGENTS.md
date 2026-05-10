# AGENTS.md

## Project

Docker-based data validation pipeline for JSONL datasets (LLM eval/training data). This is a **Turing evaluation practice submission** — the full task description is in `docs/Turing Evaluation Practice.md`.

**Goal**: Build a containerized validation gate that fails the Docker build if malformed JSONL data is detected, and succeeds with metadata labels if data is clean.

## Toolchain

- **Package manager**: `uv` (not pip/poetry)
- **Python**: 3.13 (see `.python-version`)
- **Type checker**: `basedpyright` (not mypy)
- **Validation**: `jsonschema`

## Commands

``` bash
uv sync              # install deps (creates .venv)
uv run basedpyright  # type check
uv run python main.py          # run entrypoint
uv run python scripts/validate.py  # run validation script
```

## Architecture

- `main.py` — placeholder entrypoint
- `scripts/validate.py` — **main validation logic** (currently empty). Should validate `data/datatset.jsonl` records against a schema.
- `data/datatset.jsonl` — sample dataset with intentional bad records: empty prompt, non-string completion, negative token_length
- `Dockerfile` — two-stage build: `validate` stage runs validation, `build` stage is incomplete (`FROM python:3.13-slim` only)

## Gotchas

- `pyproject.toml` `[project.scripts]` entry uses `"./scripts/validate.py"` — this is not a valid console script format (should be `module:function`). The script must be run directly via `uv run python scripts/validate.py`.
- Dataset filename has a typo: `datatset.jsonl` (not `dataset.jsonl`)
- Dockerfile `build` stage is a stub — no `COPY` or `CMD` defined yet
- No test framework configured yet

## CI

GitHub Actions (`.github/workflows/docker-publish.yml`): builds and pushes Docker image to GHCR on push to `main`, semver tags, and daily cron. Signs images with cosign.

## Branches

- `main` — default branch, CI target
- `development` — active work branch
