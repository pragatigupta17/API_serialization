'''from rest_framework import routers
from .views import StudentViewSet

router =routers.SimpleRouter()
router.register(r'student',StudentViewSet)
urlpatterns = router.urls'''


from django.urls import path, include
from .routers import router

urlpatterns=[
    path('',include(router.urls))
]