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
from .models import Employ
from .models import Client
from .models import Teacher
from .models import School
from .serializers import Pragati_serializers
from .serializers import Sajal_serializers
from .serializers import Prabha_serializers
from .serializers import Neeraj_serializers
from .serializers import Aditi_serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
    
'''class StudentViewSet(viewsets.ModelViewSet):

    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = Stu_serializers'''


#------------------------------------------------------------------------------------------------------    

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
   
    queryset = Student.objects.all()
    serializer_class = Pragati_serializers

class EmployViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    
    queryset = Employ.objects.all()
    serializer_class = Sajal_serializers
class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
   
    queryset = Client.objects.all()
    serializer_class = Prabha_serializers
class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    
    queryset = Teacher.objects.all()
    serializer_class = Neeraj_serializers
class SchoolViewSet(viewsets.ModelViewSet):
   
    queryset = School.objects.all()
    serializer_class = Aditi_serializers