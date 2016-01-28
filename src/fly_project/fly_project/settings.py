"""
Django settings for fly_project project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys
ugettext = lambda s: s

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Import variables for our application. Basically all imported variables
# have a SECRET_* prefix.
try:
    from fly_project.secret_settings import *
except ImportError:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = SECRET_DEBUG

# List of people to contact on error when DEBUG=False
ADMINS = SECRET_ADMINS

ALLOWED_HOSTS = SECRET_ALLOWED_HOSTS

# 'Sites Framework' requires this line.
SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'social.apps.django_app.default',  # python social auth
    'basepage',
    'landpage',
    'api',
    'authentication',
    'dashboard',
    'mygoals',
    'learning',
    'resources',
    'account',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'fly_project.custom_middleware.PyFlyCustomMiddleware',
]

ROOT_URLCONF = 'fly_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'social.apps.django_app.context_processors.backends',        # python social auth
                'social.apps.django_app.context_processors.login_redirect',  # python social auth
            ],
        },
    },
]

WSGI_APPLICATION = 'fly_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "fly_db",
        "USER": SECRET_DB_USER,
        "PASSWORD": SECRET_DB_PASSWORD,
        "HOST": SECRET_DB_HOST,
        "PORT": SECRET_DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#LOCALE_PATHS = (
#    os.path.join(PROJECT_PATH, 'locale/'),
#)


LANGUAGES = (
    ('en', ugettext('English')),
    ('fr', ugettext('French')),
    ('es', ugettext('Spanish')),
)


LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
)


# User uploaded content.
#

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# Email
# http://stackoverflow.com/questions/19264907/python-django-gmail-smtp-setup

EMAIL_USE_TLS = True
EMAIL_HOST = SECRET_EMAIL_HOST
EMAIL_PORT = SECRET_EMAIL_PORT
EMAIL_HOST_USER = SECRET_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = SECRET_EMAIL_HOST_USER



# Error Emailing
# https://docs.djangoproject.com/en/dev/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False, # Set to this value to prevent spam
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}



# The Google Analytics Key
GOOGLE_ANALYTICS_KEY = SECRET_GOOGLE_ANALYTICS_KEY



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Django REST Framework Configuration (Third Party)                           #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    )
}


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Python Social Auth (Third Party)                                            #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# https://github.com/omab/python-social-auth

# Facebook ( http://developers.facebook.com )
SOCIAL_AUTH_FACEBOOK_KEY = SECRET_SOCIAL_AUTH_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = SECRET_SOCIAL_AUTH_FACEBOOK_SECRET
SOCIAL_AUTH_FACEBOOK_SCOPE = SECRET_SOCIAL_AUTH_FACEBOOK_SCOPE
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = SECRET_SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS

# Twitter ( https://apps.twitter.com/app/new )
SOCIAL_AUTH_TWITTER_KEY = SECRET_SOCIAL_AUTH_TWITTER_KEY
SOCIAL_AUTH_TWITTER_SECRET = SECRET_SOCIAL_AUTH_TWITTER_SECRET

# Google ( https://console.developers.google.com/ )
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = SECRET_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = SECRET_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/dashboard'


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# django-cors-headers (Third Party)                                           #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# https://github.com/OttoYiu/django-cors-headers

CORS_ORIGIN_WHITELIST = (
    'googleapis.com',
    'google.com',
    'facebook.com',
    'twitter.com',
)