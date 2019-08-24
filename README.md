#### Login to System (POST)

###### Method that accepts username and password, returns a token. this token to be put in the header of every subsequent request

```http://localhost:8000/rest-auth/login/ POST ```



#### Create a New Flow (POST) 

###### This API creates a new Flow with access to the flow given to the user.Extract Flow ID from the API Below. This uniquely designates a Flow

```http://localhost:8000/createFlow```




#### Get Pending Flows

######This gets all flows that are currently incomplete and the current logged in user plays a role in them. Extract Flow ID from the API Below. This uniquely designates a Flow. You can have multiple flows pending

```http://localhost:8000/getPendingFlows
```



#### Get Pending Transitions in a Flow 

###### This Gets the current pending transition/stage within the flow.  This does not filter if the flow is to be actioned by current logged in user. This API is made to ascertain if there is anything pending that belongs to the user, in a specific flow.Each flow has a source and destination ,extract Source Stage ID from the API below

```
http://localhost:8000/getTransition/<flow_id>
```


#### Get Specific Fields in a Stage ( Every flow has the same fields in the same stage, so flow ID is not required)

###### Each Field will have a Unique key called Formfield, which identifies the field in this specific stage. It also has field details for rendering, and fields are sorted as the user expected them to be. 

```http://localhost:8000/FormFieldsByStage/<int:stage>
```


#### Get Completed Field Data by Flow and Stage

###### Extract Field Data by Flow and Stage 


```http://localhost:8000/getFieldData/<int:flow_id>/<int:stage>
```

#### Get Specific Field Data by Flow and formdata_id(GET), and also update it (POST)
###### Once you get the form fields, it is necessary to fill them up if they were saved by draft, or if the user went away form the app. You can extract data field wise and refill it. 

```http://localhost:8000/RetrieveUpdateFormData/<int:flow_id>/<int:formdata_id>
```


#### Create A specific Field Data(POST)

###### Once you get the form fields, some fields will be empty. You need to create the data for the formfield and the flow. Once it is created, revert to updating it. 

```http://localhost:8000/createFormData/<int:flow_id>/<int:formfield>
```


#### Validate  and Approve a Stage
###### Server side validation is performed which returns if the data is valid for a field.  If everything checks out, the stage finally gets approved

```http://localhost:8000/approveStage/<int:flow_id>/<int:stage>
```

