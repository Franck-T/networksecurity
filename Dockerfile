#FROM python:3.10-slim-buster
# Use an official Python base image and install NodeJS via apt
FROM python:3.10-slim AS base

WORKDIR /app

COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get update && pip install -r requirements.txt

CMD ["python3", "app.py"]