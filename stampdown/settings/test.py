"""Test settings."""
import logging

from . import *  # noqa: F401, F403


EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
SECRET_KEY = 'test'
SITE_ID = 1
logging.disable(logging.CRITICAL)
