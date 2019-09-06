from workflowengine.models.CustomUserModel import CustomUser
from rest_framework import serializers
from workflowengine.workflowserializers.RoleSerializer import RoleSerializer

from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from django.http import HttpResponse

from rest_framework.status import * 
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.hashers import make_password


from rest_framework.permissions import AllowAny

from django.contrib.auth.models import Group

from workflowengine.models.RoleModel import Role



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








class CustomUserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	#ole=RoleSerializer()

	class Meta:
		model = CustomUser
		#exclude=['restriction_pin', 'profilePhoto','dateOfBirth', 'user_permissions','last_login', 'is_staff', 'is_active', 'date_joined', 'groups', 'is_superuser']
		fields=['username', 'password', 'email', 'role']

	def create(self, validated_data):
		user = super(CustomUserCreateSerializer, self).create(validated_data)
		user.set_password(validated_data['password'])
		user.is_active=True
		user.is_superuser=False
		user.is_staff=False
		chosen_role=validated_data['role']

		
		if(type(chosen_role)==Role):
			role_id=chosen_role.id
		else:
			role_id=chosen_role

		if(chosen_role):
			roleObj=Role.objects.filter(id=role_id)        	
		else:
			roleObj=Role.objects.filter(primary=True)


		if(roleObj.count()==1):
			user.role=roleObj[0]
			role_name=roleObj[0].role_name
			# add user to the group matching its role.
			group=Group.objects.filter(name=role_name)
			#print(group)
			if(group.count()==1):
				user.groups.add(group[0]) 

		user.save()
		return user
	

	

		