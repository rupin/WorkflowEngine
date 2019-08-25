
from workflowengine.models.FieldModel import Field
from workflowengine.workflowserializers.ExpertiseSerializer import ExpertiseSerializer
from workflowengine.models.ExpertiseModel import Expertise


from rest_framework import generics

class getExpertise(generics.ListAPIView):   
    
    serializer_class = ExpertiseSerializer
    queryset=Expertise.objects.all()