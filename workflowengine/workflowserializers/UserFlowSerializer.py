from workflowengine.models.UserFlowModel import UserFlow
from rest_framework import serializers
from workflowengine.workflowserializers.FlowSerializer import FlowSerializer
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer
from django.conf import settings
class UserFlowSerializer(serializers.ModelSerializer):
	created_at = serializers.DateTimeField(format=settings.SITE_DATE_FORMAT, read_only=True)
	class Meta:
		model = UserFlow
		fields = "__all__"