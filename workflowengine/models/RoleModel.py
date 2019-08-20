from django.db import models

class Role(models.Model):
	role=models.CharField(max_length=50,default="")
	def __str__(self):
		return self.role
	class Meta:
		app_label="workflowengine"