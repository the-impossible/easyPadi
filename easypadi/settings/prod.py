from .base import *

ALLOWED_HOSTS = []

SECRET_KEY = config('SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

# Media files
STATIC_ROOT = '/home/easypadi/public_html/static'
MEDIA_ROOT = '/home/easypadi/public_html/media'
