from workflowengine.models.CustomUserModel import CustomUser
from rest_framework import serializers
from workflowengine.workflowserializers.RoleSerializer import RoleSerializer

from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from django.http import HttpResponse

from rest_framework.status import * 
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.ModelSerializer):
	role=RoleSerializer()	
	class Meta:
		model = CustomUser		
		exclude=['password', 'restriction_pin','email', 'last_login', 'is_staff', 'is_active', 'date_joined', 'groups', 'is_superuser']

class CustomUserPINSerializer(serializers.Serializer):

	username = serializers.CharField(required=False)
	password = serializers.CharField(required=False)
	restriction_pin = serializers.CharField(required=False)
	status_code=serializers.IntegerField(required=False)
	
	class Meta:
		model = CustomUser		
		fields=['username', 'password','restriction_pin', 'status_code']		
		#write_only_fields=['restriction_pin']
		lookup_field='pk'

		
	def update(self, instance, validated_data):
		
		blankResponse={}
		#blankResponse["username"]=""
		#blankResponse["password"]=""
		#blankResponse["restriction_pin"]=""
		
		#print(returnList)
		username=validated_data.get('username')
		password=validated_data.get('password')
		newPIN = validated_data.get('restriction_pin')
		request=self.context.get('request')
		#print(validated_data)
		unknownuser = authenticate(username=username, password=password)
		#print(unknownuser)
		
		if unknownuser is not None:#yes, a custom user exists
			if unknownuser==request.user: # person who is logged in is the person who is the unknown user			
				unknownuser.restriction_pin=make_password(newPIN)
				unknownuser.save()
				blankResponse["status_code"]=0
			else:
				raise SuspiciousOperation("Invalid User")
				blankResponse["status_code"]=2		
		else:
			#print("I am here 2")
			raise SuspiciousOperation("Not Authorised")	
			blankResponse["status_code"]=1	
		
		return blankResponse

class PINValidationSerializer(serializers.Serializer):	
	PIN_accepted=serializers.BooleanField()
	class Meta:		
		fields=['PIN_accepted']
	

	

		