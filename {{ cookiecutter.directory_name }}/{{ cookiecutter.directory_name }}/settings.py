"""Settings for this project."""
import logging
from os import environ, getenv, path
from sys import argv

from dj_database_url import config

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
SECRET_KEY = environ['SECRET_KEY']
DEBUG = 'DEBUG' in environ

TESTING = len(argv) > 1 and argv[1] == 'test'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

if not DEBUG:
    ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = ('django.contrib.sites',
                  'django.contrib.auth',
                  'django.contrib.admin',

                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'django.contrib.humanize',
                  'django.contrib.sitemaps',

                  'bootstrap3',
                  'django_nose',
                  'django_extensions',
                  'pipeline',

                  'registration',
                  'dashboard',
                  '{{ cookiecutter.directory_name }}',
                  'landing')

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware')

if TESTING:
    SITE_ID = 1
USE_ETAGS = True

ROOT_URLCONF = '{{ cookiecutter.directory_name }}.urls'
TEMPLATES = {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': (),
    'OPTIONS': {
        'context_processors': (
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages'),
        'loaders': [
                'hamlpy.template.loaders.HamlPyAppDirectoriesLoader'
        ],
        'builtins': []}},

WSGI_APPLICATION = '{{ cookiecutter.directory_name }}.wsgi.application'

DATABASES = {'default': config()}

AUTH_PASSWORD_VALIDATORS = (
    {'NAME': 'django.contrib.auth.password_validation.'
     'UserAttributeSimilarityValidator'},
    {'NAME':
     'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME':
     'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME':
     'django.contrib.auth.password_validation.NumericPasswordValidator'})

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "landing:landing"
LOGOUT_REDIRECT_URL = "landing:landing"

if TESTING:
    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
elif DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'mail@example.com'

# i18n
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static
if not TESTING:
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder')
STATICFILES_DIRS = path.join(path.dirname(__file__), '..', 'bower_components'),

STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# pipeline
PIPELINE = {
    'PIPELINE_ENABLED': TESTING or not DEBUG,
    'STYLESHEETS': {
        'application': {
            'source_filenames': ('bootstrap.less',
                                 'font-awesome/less/font-awesome.less',
                                 'landing.less',
                                 'main.less'),
            'output_filename': 'application.css'}},
    'JAVASCRIPT': {
        'application': {
            'source_filenames': ('jquery/dist/jquery.min.js',
                                 'bootstrap/js/collapse.js'),
            'output_filename': 'application.js'}},
    'COMPILERS': ('pipeline.compilers.less.LessCompiler',)}

# logging
if TESTING:
    logging.disable(logging.CRITICAL)
