from rest_framework import generics

from django.db.models import Q

from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.workflowserializers.UserFlowSerializer import UserFlowSerializer

class getPendingFlows(generics.ListAPIView):   
    
    serializer_class = UserFlowSerializer
    def get_queryset(self):
        logged_in_user = self.request.user
        return UserFlow.objects.filter(Q(user=logged_in_user) & Q(flow__completed=False))

class getCompletedFlows(generics.ListAPIView):   
    
    serializer_class = UserFlowSerializer
    def get_queryset(self):
        logged_in_user = self.request.user
        return UserFlow.objects.filter(Q(user=logged_in_user) & Q(flow__completed=True))
    	
    	