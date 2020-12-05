#!/usr/bin/env bash

set -e

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y nginx libzmq3-dev libevent-dev mariadb-common libmariadb3 build-essential libmariadb-dev python3-dev

pip3 --disable-pip-version-check --no-cache-dir install circus==0.16.1 uwsgi==2.0.18 pipenv

pipenv lock -r > /tmp/requirements.txt
pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt
rm /tmp/requirements.txt

apt-get purge -y build-essential libmariadb-dev python3-dev
apt-get autoremove -y

rm -rf /var/lib/apt/lists/*
