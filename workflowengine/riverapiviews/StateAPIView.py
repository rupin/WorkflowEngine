from rest_framework import generics
from workflowengine.riverserializers.StateSerializer import StateSerializer
from river.models import State
from workflowengine.models.FlowModel import Flow

class StateList(generics.ListAPIView):  
    
	serializer_class = StateSerializer
	def get_queryset(self):
		return State.objects.all()	

class InitialState(generics.ListAPIView):  
    
	serializer_class = StateSerializer
	def get_queryset(self):
		initialState=Flow.river.stage.initial_state
		return State.objects.filter(label=initialState)

class FinalStates(generics.ListAPIView):  
    
	serializer_class = StateSerializer
	def get_queryset(self):
		finalStates=Flow.river.stage.final_states
		return finalStates