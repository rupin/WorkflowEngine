from workflowengine.models.WorkflowTypeModel import WorkflowType
from rest_framework import serializers

class WorkflowTypeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = WorkflowType
		fields = "__all__"
		