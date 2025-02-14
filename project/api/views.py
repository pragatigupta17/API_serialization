from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
#import io

# Create your views here.
def stu_list(request):
    stu = Student.objects.all()
    print(stu)
    serializer =StudentSerializer(stu,many=True)
   # print("Serializer=",serializer)
   # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print("json_data=",json_data)
    return HttpResponse(json_data,content_type='application/json')
def stu_detail(request,pk):
    user=Student.objects.get(id=pk)
    serializer = StudentSerializer(user)
    print("Serializer=",serializer)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)
