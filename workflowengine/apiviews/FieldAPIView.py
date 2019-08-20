from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from workflowengine.models.FieldModel import Field
from workflowengine.workflowserializers.FieldSerializer import FieldSerializer
@csrf_exempt
def field_list(request):
    
    if request.method == 'GET':
        fields = Field.objects.all()
        serializer = FieldSerializer(fields, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FieldSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)