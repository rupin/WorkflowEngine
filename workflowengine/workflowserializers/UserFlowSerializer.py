from workflowengine.models.UserFlowModel import UserFlow
from rest_framework import serializers
from workflowengine.workflowserializers.FlowSerializer import FlowSerializer
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer

class UserFlowSerializer(serializers.ModelSerializer):
	created_at = serializers.DateTimeField(format="%d %B, %Y", read_only=True)
	class Meta:
		model = UserFlow
		fields = "__all__"