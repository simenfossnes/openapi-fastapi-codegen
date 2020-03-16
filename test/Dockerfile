FROM tiangolo/uvicorn-gunicorn:python3.6

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install fastapi

COPY main.py /app
COPY src /app/src
copy dist /app/dist