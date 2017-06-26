"""Production settings."""
from os import environ

from . import *  # noqa: F401, F403


ALLOWED_HOSTS = environ['ALLOWED_HOSTS'].split(',')
SECRET_KEY = environ['SECRET_KEY']
