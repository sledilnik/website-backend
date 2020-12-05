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

RUN ln -s /app/sledilnik/settings/kube.py /app/sledilnik/settings/__init__.py
RUN chown -R www-data:www-data .

RUN SECRET_KEY=nosecret python3 manage.py collectstatic --no-input

ENTRYPOINT ["circusd", "circus.ini"]