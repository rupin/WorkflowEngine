from river.models import Transition
from rest_framework import serializers
from django.conf import settings
from workflowengine.riverserializers.StateSerializer import StateSerializer
class TransitionSerializer(serializers.ModelSerializer):
	source_state=StateSerializer()
	destination_state=StateSerializer()
	class Meta:
		model =  Transition
		fields = ['source_state','destination_state']
		depth = 1