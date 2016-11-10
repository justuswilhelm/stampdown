"""WSGI config for {{ cookiecutter.project_name }} project."""
import os

from django.core.wsgi import get_wsgi_application
from dotenv import find_dotenv, load_dotenv
from whitenoise.django import DjangoWhiteNoise

load_dotenv(find_dotenv())

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "{{ cookiecutter.directory_name }}.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
