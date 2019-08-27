from workflowengine.models.FlowModel import Flow
from rest_framework import serializers
from workflowengine.workflowserializers.RoleSerializer import RoleSerializer
from workflowengine.models.UserFlowModel import UserFlow
import uuid 
from rest_framework.exceptions import PermissionDenied

class FlowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Flow
		fields = "__all__"
	def create(self, validated_data):
		parent_flow_ref=validated_data['parent_flow']
		requestRef=self.context.get('request')
		user=requestRef.user # logged in User 
		#print(validated_data)
		emptyFlow=Flow.objects.none()


		if(parent_flow_ref): # if the request has a parent flow
		#Django rest interface sends a flow object, but actual API calls will send a string
			parent_flowobj=type(parent_flow_ref) # 

			if(parent_flowobj==Flow):
				parent_flow_id=parent_flow_ref.id
			else:
				parent_flow_id=parent_flow_ref
			#print(parent_flow_id)

			#We now have access to the parent flow ID
		
			

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
				user=parent_flow_creator
			else:
				#print("OK")
				raise NotFound("Requested resource does not exist")
		
		newFlowObject=Flow.objects.create(**validated_data)			
		UserFlow.objects.create(user=user, flow=newFlowObject, creator=True)
		return newFlowObject