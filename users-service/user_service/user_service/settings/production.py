from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['your-production-domain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'pass@123'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'prod_password'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
