from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'userdb',
        'USER': 'user_service_user',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
