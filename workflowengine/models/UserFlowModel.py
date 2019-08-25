from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


from .FlowModel import Flow
import uuid

class UserFlow(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	flow=models.ForeignKey(Flow, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user.username
	class Meta:
		app_label="workflowengine"

	
