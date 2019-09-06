"""
Django settings for workflowengine project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
import django_heroku
from pathlib import Path
from google.oauth2 import service_account
import json
from .base import *


DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "w+1*!qiejv4x79k3wq)$k%q$0mpp+)6*ca7b88^$o%_)&(th-$"

# SECURITY WARNING: don't run with debug turned on in production!


SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False





# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',                      
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


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



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['localhost', '192.168.1.101']


if GOOGLE_STORAGE:


	DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
	GS_BUCKET_NAME = 'workflowenginefiles_local'
	GS_AUTO_CREATE_BUCKET=True
	with open('credentials/credentials.json') as f:
	    credentials = json.load(f)

	service_account_info = credentials
	#print(service_account_info)
	GS_CREDENTIALS = service_account.Credentials.from_service_account_info(service_account_info)
	GS_PROJECT_ID=service_account_info["project_id"]
# Activate Django-Heroku.
django_heroku.settings(locals())

