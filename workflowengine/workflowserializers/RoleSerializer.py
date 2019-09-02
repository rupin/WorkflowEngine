from workflowengine.models.RoleModel import Role
from rest_framework import serializers

class RoleSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Role
		exclude=['visible', 'index']