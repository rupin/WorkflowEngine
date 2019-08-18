from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField
from river.models import State
from .CustomUserModel import CustomUser


class Flow(models.Model):
	user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	stage= StateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.id
	class Meta:
		app_label="workflowengine"

