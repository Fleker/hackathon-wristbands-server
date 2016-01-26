# -*- coding: utf-8 -*-

from .common import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'profhacks.herokuapp.com', 'profhacks.com'] 

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')