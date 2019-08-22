from workflowengine.models.FormDataModel import FormData
from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.workflowserializers.FormDataSerializer import FormDataSerializer


from rest_framework import generics

from django.db.models import Q
from rest_framework.exceptions import PermissionDenied

from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FlowModel import Flow
from workflowengine.permissions.UserPermittedOnFlow import UserPermittedOnFlow

class FormDataList(generics.ListAPIView):  
    
	serializer_class = FormDataSerializer
	permission_classes = [UserPermittedOnFlow]
	def get_queryset(self):
		flow_id = self.kwargs['flow_id']
		
		logged_in_user = self.request.user
		
		return FormData.objects.filter(flow=flow_id)

class FormDataListByStage(generics.ListAPIView):  
    
	serializer_class = FormDataSerializer
	permission_classes = [UserPermittedOnFlow]
	def get_queryset(self):
		flow_id = self.kwargs['flow_id']
		stage_id=self.kwargs['stage']
		logged_in_user = self.request.user
		
		return FormData.objects.filter(Q(flow=flow_id) & Q(formfield__stage=stage_id))
				