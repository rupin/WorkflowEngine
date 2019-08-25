from django.db import models
from django.conf import settings
from .ExpertiseModel import Expertise
import uuid

class Expert(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	expertise=models.ForeignKey(Expertise, on_delete=models.CASCADE)
	index=models.IntegerField(default=0)
	certificate = models.FileField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		app_label="workflowengine"
		ordering=['index']
		
	
	