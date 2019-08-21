from workflowengine.models.FieldModel import Field
from rest_framework import serializers

class FieldSerializer(serializers.ModelSerializer):
	class Meta:
		model = Field
		fields = "__all__"