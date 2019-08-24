from workflowengine.models.FlowModel import Flow
from rest_framework import serializers
from workflowengine.workflowserializers.RoleSerializer import RoleSerializer
from workflowengine.models.UserFlowModel import UserFlow


class FlowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Flow
		fields = "__all__"
	def create(self, validated_data):
		#print("in create")
		newFlowObject=Flow.objects.create(**validated_data)
		user=self.context.get('request').user
		UserFlow.objects.create(user=user, flow=newFlowObject)
		return newFlowObject