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
				error['type']="validation"
				errorsList.append(error)
		return errorsList, errors	
