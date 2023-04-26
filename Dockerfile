# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /weather-bot

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Allow ubuntu to cache package downloads
RUN rm -f /etc/apt/apt.conf.d/docker-clean; \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' \
    > /etc/apt/apt.conf.d/keep-cache
# Install system dependencies
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    apt-get update \
    && apt-get --no-install-recommends -y install \
    && apt-get clean

# Install python dependencies
COPY requirements.txt .
ARG ENVIRONMENT
RUN --mount=type=cache,target=/root/.cache \
    if [ "$ENVIRONMENT" = "production" ] ; then \
        pip install -r requirements.txt ; \
    else \
        pip install -r requirements-dev.txt ; \
    fi

COPY . /weather-bot