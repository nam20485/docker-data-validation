FROM python:3.13-slim-trixie AS build
LABEL   org.opencontainers.image.version=“1.0.0” \
        dataset.schema_type=“prompt-completion” \
        dataset.lineage=“rlhf-batch-001”

COPY --from=ghcr.io/astral-sh/uv@sha256:2381d6aa60c326b71fd40023f921a0a3b8f91b14d5db6b90402e65a635053709 /uv /uvx /bin/
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app
COPY . /app

RUN uv sync --locked
RUN uv run validate data/dataset.jsonl
