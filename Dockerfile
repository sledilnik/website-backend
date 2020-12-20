ARG BASE_VERSION=v1
FROM ghcr.io/sledilnik/website-backend-base:${BASE_VERSION}

ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD . /app/
RUN mkdir -p /app/logs

RUN /app/docker/setup.sh --install && pipenv lock -r > /tmp/requirements.txt && pipenv --rm && \
    pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    /app/docker/setup.sh --cleanup

RUN ln -s /app/sledilnik/settings/kube.py /app/sledilnik/settings/__init__.py
RUN chown -R www-data:www-data .

RUN SECRET_KEY=nosecret python3 manage.py collectstatic --no-input

ENTRYPOINT ["circusd", "circus.ini"]