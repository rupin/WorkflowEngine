from workflowengine.models.UserFlowModel import UserFlow
from rest_framework import serializers
from workflowengine.workflowserializers.FlowSerializer import FlowSerializer

class UserFlowSerializer(serializers.ModelSerializer):
	flow=FlowSerializer()
	class Meta:
		model = UserFlow
		fields = "__all__"