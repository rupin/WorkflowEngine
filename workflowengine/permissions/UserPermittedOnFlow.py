from rest_framework import permissions
from workflowengine.models.UserFlowModel import UserFlow

class UserPermittedOnFlow(permissions.BasePermission):


	def has_permission(self, request, view):
		flow_id = view.kwargs.get('flow_id')
		logged_in_user = request.user
		userFlowCount=UserFlow.objects.filter(flow=flow_id, user=logged_in_user).count()
		if userFlowCount==0:
			return False
		else:
			return True