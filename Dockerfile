# syntax=docker/dockerfile:1

ARG PYTHON_MAJOR_VERSION

# Build stage
FROM python:${PYTHON_MAJOR_VERSION}-slim AS builder

RUN addgroup --system bot-admin && adduser --system --group bot-admin

COPY pyproject.toml pdm.lock /weather-bot/

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
RUN cd /weather-bot && \
    export PATH="$PATH:/root/.local/bin" && \
    python -m venv /opt/venv && \
    pdm use /opt/venv && \
    pdm install --production --frozen-lockfile --no-self && \
    chown --recursive bot-admin:bot-admin /opt/venv

# Run stage
FROM python:${PYTHON_MAJOR_VERSION}-slim as runner
# Each stage must include ARG instruction because it goes out of scope at the end of the build stage
ARG PYTHON_MAJOR_VERSION

RUN addgroup --system bot-admin && adduser --system --group bot-admin
COPY --from=builder --chown=bot-admin:bot-admin /opt/venv /opt/venv

WORKDIR /weather-bot
USER bot-admin
ENV PATH="/opt/venv/bin:${PATH}"
