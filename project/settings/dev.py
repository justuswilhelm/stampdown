"""Development settings."""
from . import *  # noqa: F401, F403


DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SECRET_KEY = 'dev'
SITE_ID = 1
