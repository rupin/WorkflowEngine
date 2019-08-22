from rest_framework import generics
from workflowengine.riverserializers.TransitionApprovalSerializer import TransitionApprovalSerializer
from river.models import TransitionApproval
from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FlowModel import Flow
from rest_framework.exceptions import PermissionDenied
from workflowengine.permissions.UserPermittedOnFlow import UserPermittedOnFlow

class getFlowHistory(generics.ListAPIView):  
    
	serializer_class = TransitionApprovalSerializer
	permission_classes = [UserPermittedOnFlow]
	def get_queryset(self):
		flow_id=self.kwargs['flow_id']		
		return TransitionApproval.objects.filter(object_id=flow_id)	
		
class availableTransitionApprovals(generics.ListAPIView):

	serializer_class = TransitionApprovalSerializer
	permission_classes = [UserPermittedOnFlow]
	def get_queryset(self):
		flow_id=self.kwargs['flow_id']
		flow=Flow.objects.get(id=flow_id)	
		return flow.river.stage.get_available_approvals(as_user=self.request.user)


		