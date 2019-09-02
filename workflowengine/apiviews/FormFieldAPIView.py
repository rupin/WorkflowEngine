from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from workflowengine.models.FormFieldModel import FormField
from workflowengine.workflowserializers.FormFieldSerializer import FormFieldSerializer


from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.db.models import Q

from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FlowModel import Flow

class FormFieldsByStage(generics.ListAPIView):   
    
    serializer_class = FormFieldSerializer

    def get_queryset(self):
        logged_in_user = self.request.user
        stage_id=self.kwargs['stage']   
        fieldsData=FormField.objects.filter(stage=stage_id).prefetch_related('field')
        return fieldsData