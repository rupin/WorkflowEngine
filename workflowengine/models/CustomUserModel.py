from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField
from river.models import State
from .RoleModel import Role

class CustomUser(AbstractUser):
	profilePhoto=models.FileField(null=True)
	dateOfBirth=models.DateField(null=True)
	role=models.ForeignKey(Role, on_delete=models.CASCADE, null=True)		
	# add additional fields in here
	class Meta:
		app_label="workflowengine"

