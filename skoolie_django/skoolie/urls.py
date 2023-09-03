
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard1, name='dashboard'),
<<<<<<< HEAD
   
=======
    path('students/update/', views.update_student, name='update_student'),
    path('attendance/', views.attendance, name='attendance')
    
>>>>>>> 14b491437fd5ffd82b75c0c9250b13690f86b980
]