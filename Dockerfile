FROM: python:3.13 name=validate
WORKDIR /app
COPY . .
RUN uv sync
RUN uv validate

FROM:python:3.13-slim name=build
