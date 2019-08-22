from rest_framework import generics
from workflowengine.riverserializers.StateSerializer import StateSerializer
from river.models import State

class StateList(generics.ListAPIView):  
    
	serializer_class = StateSerializer
	def get_queryset(self):
		return State.objects.all()	