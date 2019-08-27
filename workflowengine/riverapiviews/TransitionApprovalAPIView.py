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

from rest_framework.status import * 


class getFlowHistory(generics.ListAPIView):  
    
	serializer_class = TransitionApprovalSerializer
	permission_classes = [UserPermittedOnFlow]
	def get_queryset(self):
		flow_id=self.kwargs['flow_id']		
		return TransitionApproval.objects.filter(object_id=flow_id, status=1).order_by('transaction_date')	
		
class availableTransitionApprovals(generics.ListAPIView):

	serializer_class = TransitionApprovalSerializer
	permission_classes = [UserPermittedOnFlow]
	def get_queryset(self):
		flow_id=self.kwargs['flow_id']
		flow=Flow.objects.get(id=flow_id)
		newQS=[]	
		transitionApprovals=flow.river.stage.get_available_approvals(as_user=self.request.user)
		# for transitionApproval in transitionApprovals:
		# 	#transitionApprovals["isLastState"]=True
		# 	#transitionApprovals["isFirstState"]=True
		# 	newQS.append(transitionApprovals)
		return transitionApprovals		


	



class approveStage(APIView):
	serializer_class = ErrorSerializer
	permission_classes = [UserPermittedOnFlow]
	def get(self, request, **kwargs):
		#TODO Verify if the destination state is in the set of pending approval states
		flow_id=self.kwargs['flow_id']
		flow=Flow.objects.get(id=flow_id)
		destination_state=self.kwargs.pop('destination', None)	
		#print(destination_state)	
		status=[]
		errorcode=HTTP_200_OK
		try:
				
			source_stage, destination_state=StageFieldValidator.verifyDestinationState(self.request,destination_state, flow)
			status, errors=StageFieldValidator.validateStage(self.request,source_stage,flow)
			if(not errors):
				
				if(destination_state is None):
					responsemessage={}
					responsemessage['message']="No Pending Approval"
					responsemessage['message_type']='Success'
					errorcode=HTTP_200_OK
					status.append(responsemessage)
				else:
					flow.river.stage.approve(as_user=self.request.user, next_state=destination_state)
					finalState=Flow.river.stage.final_states
					error={}
					error['message']="Approved Successfully"
					error['message_type']='Success'
					errorcode=HTTP_200_OK
					status.append(error)	
				

		except Exception as e:
			error={}
			error['message']=str(e)
			error['message_type']='Exception'
			errorcode=HTTP_403_FORBIDDEN
			status.append(error)				
		return Response(status, status=errorcode)
	

	