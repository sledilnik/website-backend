import os
from .base import *

## read all settings from environment configmap

ALLOWED_HOSTS = list(map(str.trim, os.getenv('ALLOWED_HOSTS', '*').split(',')))
SECRET_KEY = os.getenv('SECRET_KEY')
