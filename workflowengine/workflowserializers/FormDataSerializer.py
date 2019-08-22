from workflowengine.models.FormDataModel import FormData
from rest_framework import serializers
from workflowengine.workflowserializers.FormFieldSerializer import FormFieldSerializer
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer
class FormDataSerializer(serializers.ModelSerializer):
	formfield=FormFieldSerializer()
	user=CustomUserSerializer()
	class Meta:
		model = FormData
		fields = ['file', 'text', 'updated_at','formfield', 'user']
		
	