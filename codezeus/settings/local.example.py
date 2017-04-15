"""
Local Settings
This file is to be renamed 'local.py', this file is in the .gitignore
For local/development change to:  from .development import *
For staging change to:            from .staging import *
For production change:            from .production import *
"""
from .development import *

SECRET_KEY = 'ASECRETKEYHERE'

# APPS = ('your_apps',)
# INSTALLED_APPS += APPS

# To use SQLite just delete below, it's default in base.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'codezeus',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
