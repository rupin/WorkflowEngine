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




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "w+1*!qiejv4x79k3wq)$k%q$0mpp+)6*ca7b88^$o%_)&(th-$"

# SECURITY WARNING: don't run with debug turned on in production!




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DEBUG = os.environ.get('DEBUG', default=False)
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}





# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


if GOOGLE_STORAGE:
	DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
	GS_BUCKET_NAME = 'workflowenginefiles_local'
	GS_AUTO_CREATE_BUCKET=True
	service_account_info = json.loads(os.environ.get('GS_ACCOUNT_JSON', default=False))
	GS_CREDENTIALS = service_account.Credentials.from_service_account_info(service_account_info)
	GS_PROJECT_ID=service_account_info["project_id"]


# Activate Django-Heroku.
django_heroku.settings(locals())

