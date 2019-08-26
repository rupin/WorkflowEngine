from river.models import TransitionApproval
from rest_framework import serializers
from workflowengine.workflowserializers.CustomUserSerializer import CustomUserSerializer
from workflowengine.riverserializers.StateSerializer import StateSerializer

class TransitionApprovalSerializer(serializers.ModelSerializer):
	transactioner=CustomUserSerializer()
	source_state=StateSerializer()
	destination_state=StateSerializer()	
	class Meta:
		model =  TransitionApproval
		fields = ['id', 'date_created', 'date_updated','transaction_date',
				   'status',  "source_state", "destination_state","transactioner",
				    "previous"]
		depth = 1