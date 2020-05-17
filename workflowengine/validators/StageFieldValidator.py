from workflowengine.models.FormFieldModel import FormField 
from workflowengine.models.FormDataModel import FormData 
class StageFieldValidator():

	def validateStage(request, stageID, flow):
		user=request.user
		fieldQuerySet=FormField.objects.filter(stage=stageID,mandatory=True)
		errorMessage=""
		errorsList=[]
		errors=False
		for formField in fieldQuerySet:
			error={}
			formFieldID=formField.id
			formdata=FormData.objects.filter(formfield=formFieldID,flow=flow)
			if(formdata.count()==0): # no entry found for a mandatory formfield in data
				errors=True
				error["message"]="The Field is mandatory"
				error["formfield"]=formFieldID
				error['message_type']="validation"
				errorsList.append(error)
		return errorsList, errors

	def verifyDestinationState(request, requestedDestinationStage, flow):
		user=request.user		
		pendingStageApproval=flow.river.stage.get_available_approvals(as_user=user)
		destination_state=None
		#print(pendingStageApproval.__dict__)
		if(pendingStageApproval.count()==1):
			#print("ok")
			destination_state=pendingStageApproval[0].transition.destination_state
			#print("nokay")
			source_stage=pendingStageApproval[0].transition.source_state
			return source_stage,destination_state

		if(pendingStageApproval.count()==0):			
			return None, None	

		validState=False	
		for pendingStage in pendingStageApproval:
			#print("I have more than one state")
			destination_state=pendingStage.transition.destination_state
			source_stage=pendingStage.transition.source_state
			#print(requestedDestinationStage)
			#print(destination_state)
			if(destination_state==requestedDestinationStage):
				validState=True
				break
		if(validState):
			return source_stage,destination_state
		else:
			raise ValueError('There is more than one destination state. Which state do you want to approve?')

