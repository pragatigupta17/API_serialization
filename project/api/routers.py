
from .views import StudentViewSet
from .views import EmployViewSet
from .views import ClientViewSet
from .views import TeacherViewSet
from .views import SchoolViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'student',StudentViewSet)
router.register(r'employ',EmployViewSet)
router.register(r'client',ClientViewSet)
router.register(r'teacher',TeacherViewSet)
router.register(r'school',SchoolViewSet)

urlpatterns = router.urls