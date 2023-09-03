
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('attendance/', views.attendance, name='attendance')
    # path('dashboard/', views.dashboard, name='dashboard'),
   
    # path('students/update/', views.update_student, name='update_student'),
    
    
]