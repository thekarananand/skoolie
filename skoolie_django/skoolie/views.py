from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, "skoolie/login.html")

def dashboard(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        return HttpResponse(username + "   " + password)
    
    else:
        return HttpResponse("not POST request")