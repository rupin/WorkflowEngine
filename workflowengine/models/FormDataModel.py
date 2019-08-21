
from django.db import models
from .FlowModel import Flow

from .FormFieldModel import FormField
from .CustomUserModel import CustomUser
from django.conf import settings

class FormData(models.Model):
	#pass	
	formfield=models.ForeignKey(FormField, on_delete=models.PROTECT)
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	file=models.FileField(null=True)
	text=models.CharField(max_length=500,default="",null=True) 	
	class Meta:
		app_label="workflowengine"