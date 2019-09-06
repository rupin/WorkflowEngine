from workflowengine.workflowserializers.CustomUserSerializer import *
from workflowengine.models.CustomUserModel import CustomUser

from rest_framework.viewsets import *
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse


from rest_framework import generics

from django.contrib.auth.hashers import make_password, check_password

class CustomUserAPIView(generics.ListAPIView):

	serializer_class = CustomUserSerializer
	def get_queryset(self):
		
		logged_in_user = self.request.user
		return logged_in_user

class AddUpdatePin(generics.UpdateAPIView):
	serializer_class = CustomUserPINSerializer
	
	
	def get_queryset(self):
		userID=self.request.user.id			
		retval=CustomUser.objects.filter(id=userID)		
		return retval

class ValidatePin(generics.ListAPIView):
	serializer_class = PINValidationSerializer	
	def get_queryset(self):
		userRef=self.request.user
		statusList=[]
		PIN=self.kwargs['pin'] 
		obj={}
		obj['PIN_accepted']=False
		
		print(check_password(PIN,userRef.restriction_pin))
		if(check_password(PIN,userRef.restriction_pin)):
			obj={}
			obj['PIN_accepted']=True						
			#obj['status_code']="OK"
			
		statusList.append(obj)		
		return statusList
		
class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [AllowAny]

	
	
	