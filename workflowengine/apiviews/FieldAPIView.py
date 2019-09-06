from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from workflowengine.models.FieldModel import Field
from workflowengine.workflowserializers.FieldSerializer import FieldSerializer


from rest_framework import generics
from rest_framework.permissions import IsAdminUser
    

class FieldList(generics.ListAPIView):
    lookup_field='pk'
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    