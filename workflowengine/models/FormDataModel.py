
from django.db import models
from .FlowModel import Flow
from .FieldModel import Field
from .FormModel import Form
from .CustomUserModel import CustomUser


class FormData(models.Model):
	#pass	
	form=models.ForeignKey(Form, on_delete=models.CASCADE)
	field=models.ForeignKey(Field, on_delete=models.CASCADE)
	user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)	
	file=models.FileField(null=True)
	text=models.CharField(max_length=500,default="",null=True) 	
	class Meta:
		app_label="workflowengine"