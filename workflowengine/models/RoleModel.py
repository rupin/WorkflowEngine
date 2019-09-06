from django.db import models
import uuid


class Role(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	role_name=models.CharField(max_length=50,default="")
	visible=models.BooleanField(default=False)
	index=models.IntegerField(default=0)
	primary=models.BooleanField(default=False)
	def __str__(self):
		return self.role_name
	class Meta:
		app_label="workflowengine"