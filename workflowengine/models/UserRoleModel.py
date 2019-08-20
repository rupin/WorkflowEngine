from django.db import models

class UserRole(models.Model):
	role=models.CharField(max_length=50,default="")
