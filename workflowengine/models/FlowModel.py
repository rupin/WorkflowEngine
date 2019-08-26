from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField
from river.models import State
from .CustomUserModel import CustomUser
import uuid

class Flow(models.Model):	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	stage= StateField(editable=False)
	completed=models.BooleanField(default=False)
	restricted=models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return str(self.id)
	class Meta:
		app_label="workflowengine"
		ordering=['created_at']

