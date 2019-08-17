from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

class Flow(models.Model):
	user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	stage= StateField()
	def __str__(self):
		return self.id

class Document(models.Model):
	flow=models.ForeignKey(Flow, on_delete=models.CASCADE)
	file=models.FileField()
	def __str__(self):
		return self.id


