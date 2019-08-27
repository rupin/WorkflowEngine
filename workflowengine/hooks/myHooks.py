from workflowengine.models.FlowModel import Flow
class MyHook():

	def my_callback_function(workflow_object, field_name, transition_approval=None):
		print(f"A transition happened: {transition_approval.source_state} -> {transition_approval.destination_state} by user {transition_approval.transactioner}")

	def my_callback_function_oncomplete(workflow_object, field_name):
		workflow_object.completed=True
		workflow_object.save()
		#print(type(workflow_object))
		print(f"The workflow is completed for workflow object {workflow_object} and field {field_name}")
	