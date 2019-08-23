from workflowengine.models.FormDataModel import FormData
from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FormFieldModel import FormField
from rest_framework import serializers
from workflowengine.workflowserializers.FormFieldSerializer import FormFieldSerializer
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer
class GenericFormDataSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = FormData
		fields = ['id','file', 'text', 'updated_at','formfield', 'user', 'flow']
		read_only_fields = ('formfield', 'user', 'flow')

class FormDataSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = FormData
		fields="__all__"

	
	