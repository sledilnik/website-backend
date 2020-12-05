import os
from pathlib import Path

from .base import *

## read all settings from environment configmap

ALLOWED_HOSTS = list(map(str.strip, os.getenv('ALLOWED_HOSTS', '*').split(',')))
SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(BASE_DIR, '../var/db/db.sqlite3').resolve(),
    }
}
