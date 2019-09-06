from workflowengine.models.FieldModel import Field
from rest_framework import serializers
from workflowengine.workflowserializers.WorkflowTypeSerializer import WorkflowTypeSerializer

class FieldSerializer(serializers.ModelSerializer):
	flow_type=WorkflowTypeSerializer()
	class Meta:
		model = Field
		fields = "__all__"
		depth=1