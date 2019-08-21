from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from workflowengine.models.FieldModel import Field
from workflowengine.workflowserializers.FieldSerializer import FieldSerializer


from rest_framework import generics
from rest_framework.permissions import IsAdminUser
# @csrf_exempt
# def field_list(request):
    
#     if request.method == 'GET':
#         fields = Field.objects.all()
#         serializer = FieldSerializer(fields, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = FieldSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

class FieldRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    # def get_object(self):
    #     pk=self.kwargs.get('pk')
    #     return Field.objects.get(pk=pk)

class FieldCreate(generics.CreateAPIView):
    lookup_field='pk'
    queryset = Field.objects.all()
    serializer_class = FieldSerializer



    

class FieldList(generics.ListAPIView):
    lookup_field='pk'
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    