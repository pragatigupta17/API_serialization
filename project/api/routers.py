
from .views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'student', StudentViewSet)

urlpatterns = router.urls