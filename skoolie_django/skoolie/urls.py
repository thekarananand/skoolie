
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('attendance/', views.attendance, name='attendance'),
    path('clubs/', views.clubs, name='clubs'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    
    
]