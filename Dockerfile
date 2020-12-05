FROM ghcr.io/sledilnik/website-backend-base:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD . /app/

RUN mkdir -p /app/logs

RUN pipenv lock -r > /tmp/requirements.txt && \
    pipenv --rm && \
    pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apt-get purge -y build-essential python3-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["circusd", "circus.ini"]