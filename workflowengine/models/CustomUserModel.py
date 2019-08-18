from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField
from river.models import State

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    class Meta:
    	app_label="workflowengine"

