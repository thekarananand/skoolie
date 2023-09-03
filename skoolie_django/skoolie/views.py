from django.shortcuts import render

from django.http import HttpResponse  ,HttpResponseRedirect

from .sample import sample

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "skoolie/login.html")
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            if sample[email]["PASSWORD"]==password:
                return dashboard(request, sample[email])
            else:
                return HttpResponse("Login Failed")
        except KeyError:
            return HttpResponse("Login Failed")

def dashboard(request, StudentObject):
    return HttpResponse(str(StudentObject))

def dashboard1(request):
    return render(request, "skoolie/dashboard.html", {
        "DATE" : "Sat, Sept 02"
    })
<<<<<<< HEAD
    

=======
def attendance(request):
    return render(request,"skoolie/attendance.html")

def update_student(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        subject_name = request.POST['subject_name']
        percentage = request.POST['percentage']
        

        subject_names = ["Circuit Theory", "Numerical Methods", "EMF Theory", "Electronic Devices and IC", "EMMI"]
        
        update_student_data(student_name, subject_name, percentage, subject_names)
        return HttpResponseRedirect('/students/')  
    else:
        student_data = read_student_data()
        
        subject_names = ["Circuit Theory", "Numerical Methods", "EMF Theory", "Electronic Devices and IC", "EMMI"]
        
        return render(request, 'update_student.html', {'student_data': student_data[1:], 'subject_names': subject_names})
>>>>>>> 14b491437fd5ffd82b75c0c9250b13690f86b980
