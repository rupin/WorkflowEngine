from django.db import models
from django.conf import settings
import uuid

class Expertise(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	expertise=models.CharField(max_length=200, default='')
	description=models.CharField(max_length=300, default='', null=True,blank=True)
	def __str__(self):
		return self.expertise