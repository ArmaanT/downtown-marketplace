from marketplace.settings.base import *

DEBUG = True

# Disable Django's own staticfiles handling in favour of WhiteNoise, for
# greater consistency between gunicorn and `./manage.py runserver`. See:
# http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
MIDDLEWARE.remove('django.middleware.security.SecurityMiddleware')
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE

# Fix MySQL Emoji support
DATABASES['default']['OPTIONS'] = {'charset': 'utf8mb4'}

# Honour the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow production host headers
ALLOWED_HOSTS = ['downtowns.tobaccowalla.com']
