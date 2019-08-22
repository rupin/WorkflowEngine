from river.models import TransitionApproval
from rest_framework import serializers

class  TransitionApprovalSerializer(serializers.ModelSerializer):

	class Meta:
		model =  TransitionApproval
		fields = ['id', 'date_created', 'date_updated','transaction_date',
				   'status',  "source_state", "destination_state","transactioner", "previous"]
		depth = 1