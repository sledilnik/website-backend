#!/usr/bin/env bash
set -e

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y nginx build-essential python3-dev libpq-dev libpq5
pip3 --disable-pip-version-check --no-cache-dir install circus==0.16.1 uwsgi==2.0.18 pipenv