from workflowengine.models.FlowModel import Flow
from rest_framework import serializers
from workflowengine.workflowserializers.RoleSerializer import RoleSerializer

class FlowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Flow
		fields = "__all__"