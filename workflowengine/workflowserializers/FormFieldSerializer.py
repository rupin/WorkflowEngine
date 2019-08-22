from workflowengine.models.FormFieldModel import FormField
from rest_framework import serializers
from workflowengine.workflowserializers.FieldSerializer import FieldSerializer

class FormFieldSerializer(serializers.ModelSerializer):
	#field= FieldSerializer()
	class Meta:
		model = FormField
		fields = ['field', 'id', 'mandatory', 'index']
		depth = 1