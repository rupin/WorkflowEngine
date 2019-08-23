Get Pending Flows

http://localhost:8000/getPendingFlows

Extract Flow Id from the Above Call



Get Pending Transitions in a Flow 

http://localhost:8000/getTransition/<flow_id>

Extract Source Stage ID from the above call




Get Specific Fields in a Stage ( Every flow has the same fields in the same stage, so flow ID is not required)

http://localhost:8000/FormFieldsByStage/<int:stage>

Each Field will have a Unique key called Formfield, which identifies the field in a stage. It also has field details for rendering.




Get Completed Field Data by Flow and Stage

http://localhost:8000/getFieldData/<int:flow_id>/<int:stage>


Get Specific Field Data by Flow and formdata_id(GET), and also update it (POST)

http://localhost:8000/RetrieveUpdateFormData/<int:flow_id>/<int:formdata_id>

Create A specific Field Data(POST)

http://localhost:8000/createFormData/<int:flow_id>/<int:formfield>
