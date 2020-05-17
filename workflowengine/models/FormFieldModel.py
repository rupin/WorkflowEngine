
from django.db import models
from .FlowModel import Flow
from .FieldModel import Field
from .FormModel import Form
from river.models import State
import uuid


class FormField(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	form=models.ForeignKey(Form, on_delete=models.CASCADE,default=0)
	field=models.ForeignKey(Field, on_delete=models.CASCADE,default=0)
	#stage=models.ForeignKey(State, on_delete=models.CASCADE,null=True)	
	index=models.IntegerField(default=0)
	mandatory=models.BooleanField(default=False)
	expert_search_criteria=models.BooleanField(default=False)
	include_in_summary=models.BooleanField(default=True)
	class Meta:
		app_label="workflowengine"
		ordering=['index']
		#unique_together =['form', 'field', 'stage']	



