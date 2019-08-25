from workflowengine.models.ExpertModel import Expert
from rest_framework import serializers

from workflowengine.workflowserializers.ExpertiseSerializer import ExpertiseSerializer
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer




class ExpertSerializer(serializers.ModelSerializer):	
	expertise=ExpertiseSerializer()
	#user=CustomUserSerializer()
	class Meta:
		model = Expert
		fields = ['user','expertise']
		
		