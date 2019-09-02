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
		exclude=['user']
	def create(self, validated_data):
		requestRef=self.context.get('request')
		user=requestRef.user # logged in User
		validated_data['user']=user	


		newFormDataObject, created = FormData.objects.update_or_create(
			user=user,
			formfield=validated_data.get('formfield'),
			flow=validated_data.get('flow'),

		defaults={'file': validated_data.get('file', None), 
				   'text': validated_data.get('text', None)
				  }
				  )
		return newFormDataObject	
		

	
	