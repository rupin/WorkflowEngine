

from workflowengine.workflowserializers.FlowSerializer import *


from rest_framework import generics

from django.db.models import Q
from rest_framework.exceptions import PermissionDenied

from workflowengine.models.UserFlowModel import UserFlow
from workflowengine.models.FlowModel import Flow
from workflowengine.permissions.UserPermittedOnFlow import UserPermittedOnFlow


class createFlow(generics.CreateAPIView):  
    
	serializer_class = FlowSerializer
	