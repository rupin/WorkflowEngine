from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from river.models import State



import uuid

class WorkflowType(models.Model):
	workflow_type=models.CharField(max_length=20)
	start_stage=models.ForeignKey(State, on_delete=models.CASCADE,null=True, blank=True)	
	def __str__(self):
		return self.workflow_type
	class Meta:
		app_label="workflowengine"

	