from .base import *
from .secrets import *

INSTALLED_APPS += [
    'django_extensions'
]

# DEBUG = False

# ALLOWED_HOSTS = ["127.0.0.1"]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'sledilnik',
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'default',
#         'TIMEOUT': 60,
#     }
# }

CACHE_MIDDLEWARE_SECONDS = 0
