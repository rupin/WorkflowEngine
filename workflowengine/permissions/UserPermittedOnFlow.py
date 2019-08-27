from rest_framework import permissions
from workflowengine.models.UserFlowModel import UserFlow

class UserPermittedOnFlow(permissions.BasePermission):


	def has_permission(self, request, view):
		flow_id = view.kwargs.get('flow_id')
		return UserFlow.doesUserHaveAccess(request,flow_id)