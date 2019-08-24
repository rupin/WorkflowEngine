from rest_framework import serializers
class ErrorSerializer(serializers.Serializer):
	message=serializers.CharField(max_length=200)
	formfield=serializers.IntegerField()
	errortype=serializers.CharField(max_length=200)
	
		
		