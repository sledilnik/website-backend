FROM python:3.9.6-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ADD . /app/

# this installs runtimpe dependencies and clean build dependencies, to keep image small
RUN /app/docker/setup.sh --install && /app/docker/setup.sh --cleanup
