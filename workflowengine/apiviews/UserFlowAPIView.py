from rest_framework import generics

from django.db.models import Q

from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FlowModel import Flow
from workflowengine.workflowserializers.FlowSerializer import FlowSerializer
from workflowengine.workflowserializers.FlowSerializer import FlowSerializer

class getPendingFlows(generics.ListAPIView):   
    
    serializer_class = FlowSerializer
    def get_queryset(self):
        logged_in_user = self.request.user
        return Flow.objects.filter(Q(userflow__user=logged_in_user) & Q(completed=False)).order_by('-created_at')

class getCompletedFlows(generics.ListAPIView):   
    
    serializer_class = FlowSerializer
    def get_queryset(self):
        logged_in_user = self.request.user
        return UserFlow.objects.filter(Q(userflow__user=logged_in_user) & Q(completed=True)).order_by('-created_at')
    	
    	