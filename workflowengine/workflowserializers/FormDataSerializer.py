from workflowengine.models.FormDataModel import FormData
from rest_framework import serializers
from workflowengine.workflowserializers.FormFieldSerializer import FormFieldSerializer
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer
class FormDataSerializer(serializers.ModelSerializer):
	formfield=FormFieldSerializer()
	user=CustomUserSerializer()
	class Meta:
		model = FormData
		fields = ['file', 'text', 'flow', 'created_at', 'updated_at','formfield', 'user']

	def to_representation(self, obj):
		"""Move fields from profile to user representation."""
		

		representation = super().to_representation(obj)
		formfield_representation = representation.pop('formfield')
		for key in formfield_representation:
			representation[key] = formfield_representation[key]

		return representation