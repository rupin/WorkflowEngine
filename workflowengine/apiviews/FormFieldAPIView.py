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
class FormFieldList(generics.ListAPIView):   
    
    serializer_class = FormFieldSerializer

    def get_queryset(self):
        logged_in_user = self.request.user
        
        in_progress_flows=UserFlow.objects.filter(
        											Q(user=logged_in_user) &
        											Q(flow__completed=False)
        										).values('flow__stage')

        fieldsData=FormField.objects.filter(Q(stage__in=in_progress_flows))

        return fieldsData