
from django.db import models
from .FlowModel import Flow
from .FieldModel import Field
from .FormModel import Form


class FormField(models.Model):
	#pass	
	form=models.ForeignKey(Form, on_delete=models.CASCADE,default=0)
	field=models.ForeignKey(Field, on_delete=models.CASCADE,default=0)	
	index=models.IntegerField(default=0) 	
	class Meta:
		app_label="workflowengine"