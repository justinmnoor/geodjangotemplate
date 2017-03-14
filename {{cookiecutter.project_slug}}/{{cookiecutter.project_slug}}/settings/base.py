# ==================================================================================================
# DJANGO 1.10.5 COMMON SETTINGS
# https://docs.djangoproject.com/en/1.10/topics/settings/
# ==================================================================================================


# IMPORT MODULES
# ==================================================================================================

import boto3
import json
import os


# ENVIRONMENT CONFIGURATION
# importing environment variables from json files
# ==================================================================================================

with open('{{cookiecutter.project_slug}}/config/aws_config.json') as f:
    aws_config = json.loads(f.read())

with open('{{cookiecutter.project_slug}}/config/db_config.json') as f:
    db_config = json.loads(f.read())

with open('{{cookiecutter.project_slug}}/config/dj_config.json') as f:
    dj_config = json.loads(f.read())

def get_dj_config(setting, dj_config=dj_config):
    return dj_config[setting]

def get_db_config(db_config=db_config):
    return db_config

def get_aws_config(setting, aws_config=aws_config):
    return aws_config[setting]


# KEY ENVIRONMENT VARIABLES	
# ==================================================================================================
"""
Find your environment variable settings files in:
'{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/config/'
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = get_dj_config("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = get_dj_config("DJANGO_ALLOWED_HOSTS")

AWS_ACCESS_KEY_ID = get_aws_config("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = get_aws_config("AWS_SECRET_ACCESS_KEY")


# AWS CONFIGURATION
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
# ==================================================================================================

AWS_S3_CUSTOM_DOMAIN = get_aws_config("AWS_S3_CUSTOM_DOMAIN")

AWS_STORAGE_BUCKET_NAME = get_aws_config("AWS_STORAGE_BUCKET_NAME")

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# APP CONFIGURATION
# https://docs.djangoproject.com/en/1.10/ref/applications
# ==================================================================================================

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]

MY_APPS = []

THIRD_PARTY_APPS = [
    'crispy_forms',
    'storages',
]

INSTALLED_APPS = DJANGO_APPS + MY_APPS + THIRD_PARTY_APPS

# MIDDLEWARE CONFIGURATION
# ==================================================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# TEMPLATE CONFIGURATION
# ==================================================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# DATABASE CONFIGURATION
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# ==================================================================================================

DATABASES = get_db_config(db_config=db_config)


# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
# ==================================================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# INTERNATIONALIZATION
# https://docs.djangoproject.com/en/1.10/topics/i18n/
# ==================================================================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATIC FILES CONFIGURATION
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# ==================================================================================================

STATIC_ROOT = os.path.join('static/')

STATIC_URL = '/static/'

STATICFILES_DIRS = ['{{cookiecutter.project_slug}}/static/']

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA CONFIGURATION
# https://docs.djangoproject.com/en/1.10/ref/settings/#media-root
# ==================================================================================================

MEDIA_ROOT = os.path.join('media/')

MEDIA_URL = '/media/'


# URL CONFIGURATION
# https://docs.djangoproject.com/en/1.10/ref/settings/#root-urlconf
# ==================================================================================================

ROOT_URLCONF = '{{cookiecutter.project_slug}}.urls'


# WSGI CONFIGURATION
# https://docs.djangoproject.com/en/1.10/ref/settings/#wsgi-application
# ==================================================================================================

WSGI_APPLICATION = '{{cookiecutter.project_slug}}.wsgi.application'


