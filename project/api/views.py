'''from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import Stu_serializers
from rest_framework.renderers import JSONRenderer'''
#from rest_framework.parsers import JSONParser
#import io

# Create your views here.
'''def stu_list(request):
    stu = Student.objects.all()
    print(stu)
    serializer =Stu_serializers(stu,many=True)
   # print("Serializer=",serializer)
   # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print("json_data=",json_data)
    return HttpResponse(json_data,content_type='application/json')
def stu_detail(request,pk):
    user=Student.objects.get(id=pk)
    serializer = Stu_serializers(user)
    print("Serializer=",serializer)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)'''
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import Stu_serializers

@csrf_exempt
def stu_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = Stu_serializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Stu_serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
   
@csrf_exempt
def stu_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Stu_serializers(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Stu_serializers(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = Stu_serializers(snippet, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        stu.delete()
        return HttpResponse(status=204)