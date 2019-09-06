

from workflowengine.workflowserializers.ExpertSerializer import ExpertSerializer
from workflowengine.models.ExpertModel import Expert


from rest_framework import generics

class getUserExpertInfo(generics.ListAPIView):   
    
    serializer_class = ExpertSerializer
    def get_queryset(self):
    	user=self.kwargs['user']
    	return Expert.objects.filter(user=user).prefetch_related('user', 'expertise')