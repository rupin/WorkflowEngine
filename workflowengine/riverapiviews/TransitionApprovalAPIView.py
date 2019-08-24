from rest_framework import generics
from workflowengine.riverserializers.TransitionApprovalSerializer import TransitionApprovalSerializer
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer
from river.models import TransitionApproval
from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FlowModel import Flow
from rest_framework.exceptions import PermissionDenied
from workflowengine.permissions.UserPermittedOnFlow import UserPermittedOnFlow

from workflowengine.validators.StageFieldValidator import StageFieldValidator

from workflowengine.validators.ErrorSerializer import ErrorSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


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


	



class approveStage(APIView):
	serializer_class = ErrorSerializer
	permission_classes = [UserPermittedOnFlow]
	def get(self, request, **kwargs):
		flow_id=self.kwargs['flow_id']
		flow=Flow.objects.get(id=flow_id)
		stageid=self.kwargs['stage']	
		errorList, errors=StageFieldValidator.validateStage(self.request,stageid,flow)
		#print(errorList)
		if(not errors):
			#print("Approving")
			try:
				flow.river.stage.approve(as_user=self.request.user)
			except Exception as e:
				error={}
				error['message']=str(e)
				error['errortype']='exception'
				errorList.append(error)				
		return Response(errorList)
	