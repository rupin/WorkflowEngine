from workflowengine.models.CustomUserModel import CustomUser
from rest_framework import serializers
from workflowengine.workflowserializers.RoleSerializer import RoleSerializer


class CustomUserSerializer(serializers.ModelSerializer):
	role=RoleSerializer()	
	class Meta:
		model = CustomUser		
		exclude=['password', 'restriction_pin','email', 'last_login', 'is_staff', 'is_active', 'date_joined', 'groups', 'is_superuser']
