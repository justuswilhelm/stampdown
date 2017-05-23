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
    'bootstrap3',
    'django_extensions',
)

FIRST_PARTY_APPS = (
    "account",
    "common",
    "dashboard",
    "landing",
    "project",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + FIRST_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
)

# URL
ROOT_URLCONF = 'project.urls'

# WSGI
WSGI_APPLICATION = 'project.wsgi.application'

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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = (
    path.join(BASE_DIR, 'bower_components'),
)
STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
