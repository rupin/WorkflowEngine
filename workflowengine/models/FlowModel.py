from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField
from river.models import State
from .CustomUserModel import CustomUser
from .WorkflowTypeModel import WorkflowType
import uuid

class Flow(models.Model):	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	stage= StateField(editable=False)
	completed=models.BooleanField(default=False)
	restricted=models.BooleanField(default=True)
	flow_type=models.ForeignKey(WorkflowType, on_delete=models.PROTECT, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	parent_flow = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
	flow_name=models.CharField(max_length=50,default="",null=True, blank=True) 
	def __str__(self):
		return str(self.flow_name)
	class Meta:
		app_label="workflowengine"
		ordering=['created_at']

	def putFlowOnTrack(self, user):
		destination_state=self.flow_type.start_stage.id		
		self.river.stage.approve(as_user=user, next_state=destination_state, god_mod=True)






