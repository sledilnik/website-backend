import os
from pathlib import Path

from .base import *

DEBUG = False

ALLOWED_HOSTS = list(map(str.strip, os.getenv('ALLOWED_HOSTS', '*').split(',')))
SECRET_KEY = os.getenv('SECRET_KEY')

STATIC_ROOT = Path(BASE_DIR, '../static').resolve()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASS'),
        'HOST': 'postgresql.default.svc.cluster.local',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default',
        'TIMEOUT': 60,
    }
}

CACHE_MIDDLEWARE_SECONDS = 60
