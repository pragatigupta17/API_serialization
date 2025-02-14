from django.urls import path
from . import views
urlpatterns =[
    path('stu_list/',views.stu_list),
    path('stu_detail/<int:pk>',views.stu_detail),

]