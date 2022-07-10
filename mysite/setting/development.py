from mysite.settings import *
import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')


# INSTALLED_APPS[]


# Sites Framework
SITE_ID = 2


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'  # setting static file for production mode.


# Media files (for upload media files form users)

MEDIA_ROOT = BASE_DIR / 'media'  # MEDIA_ROOT is the path to the root directory where the files are getting stored.
