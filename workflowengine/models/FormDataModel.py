
from django.db import models
from .FlowModel import Flow

from .FormFieldModel import FormField
from .CustomUserModel import CustomUser
from .FlowModel import Flow
from django.conf import settings
import uuid

class FormData(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	formfield=models.ForeignKey(FormField, on_delete=models.PROTECT)
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	flow=models.ForeignKey(Flow,on_delete=models.PROTECT,null=True, blank=True)
	file=models.FileField(null=True, blank=True)
	text=models.CharField(max_length=500,default="",null=True, blank=True) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
	class Meta:
		app_label="workflowengine"