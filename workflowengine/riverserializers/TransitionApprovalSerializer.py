from river.models import TransitionApproval
from rest_framework import serializers
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer
from workflowengine.riverserializers.StateSerializer import StateSerializer

from django.conf import settings

class TransitionApprovalSerializer(serializers.ModelSerializer):
	transactioner=CustomUserSerializer()
	source_state=StateSerializer()
	destination_state=StateSerializer()	
	date_created=serializers.DateTimeField(format=settings.SITE_DATE_FORMAT, read_only=True)
	date_updated=serializers.DateTimeField(format=settings.SITE_DATE_FORMAT, read_only=True)
	transaction_date=serializers.DateTimeField(format=settings.SITE_DATE_FORMAT, read_only=True)
	class Meta:
		model =  TransitionApproval
		fields = ['id', 'date_created', 'date_updated','transaction_date',
				   'status',  "source_state", "destination_state","transactioner",
				    "previous"]
		depth = 1