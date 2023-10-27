from .base import *

ALLOWED_HOSTS = ["www.easypadi.com", "easypadi.com"]

SECRET_KEY = config('SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Media files
STATIC_URL = '/static/'
#STATIC_ROOT = '/home/kadpwtrj/easypadi.com/public_html/static'
STATIC_ROOT = '/home/kadpwtrj/easypadi.com/Static'
MEDIA_ROOT = '/home/kadpwtrj/easypadi.com/public_html/media'
