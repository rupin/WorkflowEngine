from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField
from river.models import State
from .FlowModel import Flow


class Form(models.Model):
	flow=models.ForeignKey(Flow, on_delete=models.CASCADE)
	stage=models.ForeignKey(State, on_delete=models.CASCADE)
	description=models.CharField(max_length=200,default="")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.id
	class Meta:
		app_label="workflowengine"