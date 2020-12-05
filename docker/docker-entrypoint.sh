#!/bin/sh

set -e

WAIT_DB=${SEAHELP_DB_HOST:-db}:${SEAHELP_DB_PORT:-3306}

>&2 echo "Waiting for database: ${WAIT_DB}"
./bin/wait-for-it.sh -t 30 ${WAIT_DB}
>&2 echo "Database is ready"

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python manage.py migrate --noinput
fi

mkdir -p logs/circus
exec circusd circus.ini