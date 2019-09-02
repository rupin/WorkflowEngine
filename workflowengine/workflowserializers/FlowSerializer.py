from workflowengine.models.FlowModel import Flow
from workflowengine.models.WorkflowTypeModel import WorkflowType
from rest_framework import serializers
from workflowengine.workflowserializers.RoleSerializer import RoleSerializer
from workflowengine.models.UserFlowModel import UserFlow
import uuid 
from rest_framework.exceptions import PermissionDenied
from workflowengine.hooks.myHooks import MyHook
from django.conf import settings
class FlowSerializer(serializers.ModelSerializer):
	created_at = serializers.DateTimeField(format=settings.SITE_DATE_FORMAT, read_only=True)
	class Meta:
		model = Flow
		fields = "__all__"
	def create(self, validated_data):
		parent_flow_ref=validated_data['parent_flow']
		flow_type=validated_data['flow_type']
		requestRef=self.context.get('request')
		user=requestRef.user # logged in User 		
		emptyFlow=Flow.objects.none()

		# Returns Flow type Object or the primary flow type
		flow_type=WorkflowType.getFlowTypeObject(flow_type)

		if(parent_flow_ref): # if the request has a parent flow
		#Django rest interface sends a flow object, but actual API calls will send a string
			parent_flowobj=type(parent_flow_ref) # 

			if(parent_flowobj==Flow):
				parent_flow_id=parent_flow_ref.id
			else:
				parent_flow_id=parent_flow_ref
			#print(parent_flow_id)

			#We have access to the parent flow ID
		
			

			# Check if the current user has access to the parent flow

			userHasAccess=UserFlow.doesUserHaveAccess(requestRef, parent_flow_id)
			if(not userHasAccess):
				raise PermissionDenied("You are not authorised")

			# Find who created this flow, they will be the given access of the new flow

			parent_flow_object=UserFlow.objects.filter(flow=parent_flow_id, creator=True)
			#print(parent_flow_object)
			if(parent_flow_object.count()==1):
				parent_flow_creator=parent_flow_object[0].user
				#updated the user object to the flow creator of the parent flow	
				# because the user who created the parent flow should be the creator of the 
				# new child flow !! BIG ASSUMPTION	!!		
				user=parent_flow_creator
			else:
				#print("OK")
				raise NotFound("Requested resource does not exist")

		validated_data['flow_type']=flow_type
		newFlowObject=Flow.objects.create(**validated_data)	
		UserFlow.objects.create(user=user, flow=newFlowObject, creator=True)

		newFlowObject.river.stage.hook_post_transition(MyHook.my_callback_function)
		newFlowObject.river.stage.hook_post_complete(MyHook.my_callback_function_oncomplete)
		
		
		# Depending on WorkflowType property, the correct starting stage is figured out and the 
		# flow is put on the correct track. 
		newFlowObject.putFlowOnTrack(user)
		
		
		return newFlowObject