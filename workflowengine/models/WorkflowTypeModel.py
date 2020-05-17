from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from river.models import State



import uuid

class WorkflowType(models.Model):
	workflow_type=models.CharField(max_length=20)
	#start_stage=models.ForeignKey(State, on_delete=models.CASCADE,null=True, blank=True)	
	primary=models.BooleanField(default=False)
	def __str__(self):
		return self.workflow_type
	class Meta:
		app_label="workflowengine"

	def getFlowTypeObject(flow_type):

		if(not flow_type):
			primaryFlowType=WorkflowType.objects.filter(primary=True)
			if(primaryFlowType.count()==1):
				#print(primaryFlowType)
				return primaryFlowType[0]
			else:
				raise Exception("Please set one (and only one) Flow Type as Primary")
		else:

			object_type=type(flow_type)
			if(object_type==WorkflowType):
				flow_type_id=flow_type.id
			else:
				flow_type_id=flow_type	

			FlowType=WorkflowType.objects.filter(id=flow_type_id)
			if(FlowType.count()==1):
				return FlowType[0]
			else:
				raise Exception("Incorrect Flow type")	

		

	