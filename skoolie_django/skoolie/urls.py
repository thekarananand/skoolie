
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard1, name='dashboard'),
   
    path('students/update/', views.update_student, name='update_student'),
    path('attendance/', views.attendance, name='attendance')
    
]