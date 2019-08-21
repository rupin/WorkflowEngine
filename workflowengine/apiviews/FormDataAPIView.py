from workflowengine.models.FormDataModel import FormData
from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.workflowserializers.FormDataSerializer import FormDataSerializer


from rest_framework import generics

from django.db.models import Q
from rest_framework.exceptions import PermissionDenied

from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FlowModel import Flow

class FormDataList(generics.ListAPIView):  
    
	serializer_class = FormDataSerializer
	def get_queryset(self):
		flow_id = self.kwargs['flow_id']
		logged_in_user = self.request.user
		doesUserHaveAccess=UserFlow.objects.filter(flow=flow_id, user=logged_in_user).count()
		#print(doesUserHaveAccess)
		if doesUserHaveAccess!=0:
			return FormData.objects.filter(flow=flow_id)
		else:
			raise PermissionDenied()		