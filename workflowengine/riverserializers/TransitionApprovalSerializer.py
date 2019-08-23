from river.models import TransitionApproval
from rest_framework import serializers
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer

class  TransitionApprovalSerializer(serializers.ModelSerializer):
	transactioner=CustomUserSerializer()
	class Meta:
		model =  TransitionApproval
		fields = ['id', 'date_created', 'date_updated','transaction_date',
				   'status',  "source_state", "destination_state","transactioner", "previous"]
		depth = 1