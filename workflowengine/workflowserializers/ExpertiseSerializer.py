from workflowengine.models.ExpertiseModel import Expertise
from rest_framework import serializers




class ExpertiseSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Expertise
		fields = "__all__"
		