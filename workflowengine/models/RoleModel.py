from django.db import models
import uuid


class Role(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	role=models.CharField(max_length=50,default="")
	def __str__(self):
		return self.role
	class Meta:
		app_label="workflowengine"