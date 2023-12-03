# syntax = docker/dockerfile:1.4

FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends git

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]

EXPOSE 8000