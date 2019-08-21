from workflowengine.models.CustomUserModel import CustomUser
from rest_framework import serializers
from workflowengine.workflowserializers.RoleSerializer import RoleSerializer


class CustomUserSerializer(serializers.ModelSerializer):
	role=RoleSerializer()	
	class Meta:
		model = CustomUser
		fields = ['role']


	def to_representation(self, obj):
		"""Move fields from profile to user representation."""
		representation = super().to_representation(obj)
		profile_representation = representation.pop('role')
		for key in profile_representation:
			representation[key] = profile_representation[key]

		return representation