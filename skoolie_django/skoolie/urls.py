
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard1, name='dashboard'),
   
]