from workflowengine.models.FormDataModel import FormData
from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FormFieldModel import FormField
from workflowengine.workflowserializers.FormDataSerializer import *


from rest_framework import generics

from django.db.models import Q
from rest_framework.exceptions import PermissionDenied

from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FlowModel import Flow
from workflowengine.permissions.UserPermittedOnFlow import UserPermittedOnFlow

from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,ListModelMixin


class FormDataView(generics.ListAPIView):  
    
	serializer_class = GenericFormDataSerializer
	permission_classes = [UserPermittedOnFlow]
	def get_queryset(self):
		flow_id = self.kwargs['flow_id']
		formfield = self.kwargs['formfield']		
		logged_in_user = self.request.user		
		return FormData.objects.filter(flow=flow_id, formfield=formfield).prefetch_related('formfield')

class FormDataByStage(generics.ListAPIView):  
    
	serializer_class = GenericFormDataSerializer
	permission_classes = [UserPermittedOnFlow]
	def get_queryset(self):
		flow_id = self.kwargs['flow_id']
		stage_id=self.kwargs['stage']
		logged_in_user = self.request.user
		
		return FormData.objects.filter(Q(flow=flow_id) & Q(formfield__stage=stage_id))



# class RetrieveUpdateFormData(generics.RetrieveUpdateAPIView):  
    
# 	serializer_class = GenericFormDataSerializer
# 	permission_classes=[UserPermittedOnFlow]	
# 	lookup_field='pk'
# 	def get_queryset(self):
# 		user = self.request.user
# 		pk=self.kwargs['pk']
# 		flow_id=self.kwargs['flow_id']
# 		#flow_id=self.kwargs['flow_id']		
# 		return FormData.objects.filter(id=pk, flow=flow_id)

	

class createFormData(generics.CreateAPIView):  
    
	serializer_class = FormDataSerializer
	permission_classes = [UserPermittedOnFlow]
	

	
		






		
	
				