"""Production settings."""
from os import environ

from . import *  # noqa: F401, F403


ALLOWED_HOSTS = environ['ALLOWED_HOSTS'].split(',')
SECRET_KEY = environ['SECRET_KEY']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
