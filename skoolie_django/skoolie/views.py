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
    

