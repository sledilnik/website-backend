from .base import *
from .secrets import *

INSTALLED_APPS += [
    'django_extensions'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sledilnik',
    }
}
