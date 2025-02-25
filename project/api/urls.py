from django.urls import path
from .import views
from .views import Stu_List,Stu_Detail


urlpatterns =[
  #  path('stu_list/',views.stu_list),
  # path('stu_detail/<int:pk>/',views.stu_detail),
    path('stu_list/',Stu_List.as_view(),name='stu_list'),
    path('stu_detail/<int:pk>/',Stu_Detail.as_view(),name='stu_detail')

  

]