"""Settings for this project."""
from os import path

from dj_database_url import config
from dotenv import (
    find_dotenv,
    load_dotenv,
)


load_dotenv(find_dotenv())


BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

DJANGO_APPS = (
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.admin',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
)

THIRD_PARTY_APPS = (
    'django_extensions',
    'tz_detect',
)

FIRST_PARTY_APPS = (
    "account",
    "common",
    "dashboard",
    "landing",
    "timestamp",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + FIRST_PARTY_APPS

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'tz_detect.middleware.TimezoneMiddleware',
)

# URL
ROOT_URLCONF = 'stampdown.urls'

# WSGI
WSGI_APPLICATION = 'stampdown.wsgi.application'

# Tempates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (),
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'),
            'loaders': [
                'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
            ],
            'builtins': [],
        },
    }
]

# DB
DATABASES = {
    'default': config(),
}

# Auth
AUTH_PASSWORD_VALIDATORS = (
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator'},
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
)
AUTH_USER_MODEL = 'account.EmailUser'
LOGIN_REDIRECT_URL = "landing:landing"
LOGIN_URL = "account:login"
LOGOUT_REDIRECT_URL = "landing:landing"

# Email
DEFAULT_FROM_EMAIL = 'mail@justusperlwitz.com'

# i18n
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Berlin'
USE_TZ = True
LANGUAGES = (
    ('de-de', 'German'),
    ('en-us', 'English'),
    ('jp-ja', 'Japanese'),
)

TZ_DETECT_COUNTRIES = (
    'DE',
    'JP',
    'US',
)

# static
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = (
)
STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            "level": 'WARNING',
        },
    },
    'loggers': {
        'django': {
            'handlers': (
                'console',
            ),
        },
    }
}

# timezone
