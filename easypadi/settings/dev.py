from .base import *

ALLOWED_HOSTS = ["*"]

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
MEDIA_ROOT = os.path.join(BASE_DIR, 'Static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
MEDIA_URL = "/media/"
STATIC_URL = "static/"
STATICFILES_DIRS = [STATIC_DIR,]