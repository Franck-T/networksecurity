#FROM python:3.10-slim-buster
# Use an official Python base image and install NodeJS via apt
FROM python:3.10-slim AS base

# Avoid python buffering stdout/stderr
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

#COPY . /app
COPY hello.py /app

#RUN apt update -y && apt install awscli -y

#RUN apt-get update && apt-get install -y git

#RUN pip install -r requirements.txt

#CMD ["python3", "app.py"]

EXPOSE 8080

CMD ["python3", "hello.py"]