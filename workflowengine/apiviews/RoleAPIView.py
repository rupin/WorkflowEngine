from workflowengine.workflowserializers.RoleSerializer import RoleSerializer
from workflowengine.models.RoleModel import Role
from workflowengine.bg_tasks.tasks import *

from rest_framework import generics

class RoleAPIView(generics.ListAPIView):
	serializer_class = RoleSerializer
	def get_queryset(self):
		list.delay()
		return Role.objects.filter(visible=True).order_by('index')