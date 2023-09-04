from django.urls import path
from . import views

urlpatterns = [
    path('url/task/', views.my_list, name='my_list'),
    path('',views.home),
]