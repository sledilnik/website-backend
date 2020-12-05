import os
from .base import *

## read all settings from environment configmap

SECRET_KEY = os.getenv('SECRET_KEY')
