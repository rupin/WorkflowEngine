from river.models import TransitionApproval
from rest_framework import serializers
from workflowengine.workflowserializers.CustomUserSerializer import LimitedUserSerializer
from workflowengine.riverserializers.StateSerializer import StateSerializer
from workflowengine.riverserializers.TransitionSerializer import TransitionSerializer
from django.conf import settings

class TransitionApprovalSerializer(serializers.ModelSerializer):
	transactioner=LimitedUserSerializer()	
	date_created=serializers.DateTimeField(format=settings.SITE_DATE_FORMAT, read_only=True)
	date_updated=serializers.DateTimeField(format=settings.SITE_DATE_FORMAT, read_only=True)
	transaction_date=serializers.DateTimeField(format=settings.SITE_DATE_FORMAT, read_only=True)
	transition=TransitionSerializer()
	class Meta:
		model =  TransitionApproval
		fields = ['id', 'date_created', 'date_updated','transaction_date',
				   'status',  'transition',"transactioner",
				    "previous"]
		depth = 1