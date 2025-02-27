'''from .models import Student
from .serializers import Stu_serializers
from rest_framework import generics


class Stu_List(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Stu_serializers


class Stu_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Stu_serializers'''


from .models import Student
from .serializers import Stu_serializers
from rest_framework import viewsets
    
class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = Stu_serializers