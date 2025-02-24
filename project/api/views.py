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

"""from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import Stu_serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET','POST'])
def stu_list(request):
    """#List all code snippets, or create a new snippet.
"""
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = Stu_serializers(snippets, many=True)
       # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data, )

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = Stu_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
           # return JsonResponse(serializer.data, status=201)
            #return JsonResponse(serializer.errors, status=400)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','PUT','PATCH','DELETE'])
def stu_detail(request, pk):
    """
   # Retrieve, update or delete a code snippet.
"""
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
       # return HttpResponse(status=404)
        return Response(status=404)

    if request.method == 'GET':
        serializer = Stu_serializers(snippet)
       # return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = Stu_serializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return Response(serializer.data)
       # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        #data = JSONParser().parse(request)
        serializer = Stu_serializers(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return Response(serializer.data)
        #return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        #return HttpResponse(status=204)
        return Response({'msg':'data deleted'},status=204)"""
from .models import Student
from .serializers import Stu_serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Stu_List(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Student.objects.all()
        serializer = Stu_serializers(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Stu_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Stu_Detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stu_Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stu_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)