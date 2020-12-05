FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ADD . /app/
ADD ./docker/install-deps.sh /install-deps.sh
ADD ./docker/docker-entrypoint.sh /docker-entrypoint.sh

RUN /install-deps.sh && rm /install-deps.sh
RUN SKIP_DB=true python manage.py collectstatic --noinput

ENTRYPOINT ["/docker-entrypoint.sh"]