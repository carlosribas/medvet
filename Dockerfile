# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.7-slim-buster

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED=1

# Install system packages.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install the project requirements.
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Copy the source code of the project into the container.
COPY . .

# Run entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
