from django.shortcuts import render

from django.http import HttpResponse  ,HttpResponseRedirect

from .sample import sample
from .utils import PresentageAttendance, ReadAttendance

passStudentObject = {}

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

    DETAINED = attendance_display(StudentObject["DATA"]["ROLLNO"], StudentObject["SUBJECTS"])

    if DETAINED == 1 :
        ATTENDANCE = f"Detained in 1 Subject"
        ATTENDANCE_SHADE = "#FFC8C8"
    
    elif DETAINED > 1 :
        ATTENDANCE = f"Detained in {DETAINED} Subjects"
        ATTENDANCE_SHADE = "#FFC8C8"
    else:
        ATTENDANCE = "All Good"
        ATTENDANCE_SHADE = "#C8FFC8"

    return render(request, "skoolie/dashboard.html", {
        "GREET" : "Evening",
        "DATE" : "Mon, Sept 04",
        "NAME" : StudentObject["PREFERED NAME"],
        "ATTENDANCE" : ATTENDANCE,
        "ATTENDANCE_SHADE" : ATTENDANCE_SHADE,

        "rollno" : StudentObject["DATA"]["ROLLNO"]
    })
    
def attendance_display(rollno, subjects):
    n = 0
    for subject in subjects:
        if int(PresentageAttendance(rollno, subject)) < 75:
            n = n + 1

    return n
def colouratt(percent):
    if percent>=75:
        return '#C8FFC8'
    else:
        return '#FFC8C8'
def attendance(request):
    if request.method == "POST":
        rollno = request.POST.get('rollno', '')  # Use get() to avoid KeyError

        present = []
        total = []
        percentage = []

        for subject in ["CT", "DST"]:
            try:
                lst = ReadAttendance(rollno, subject)
                total.append(lst[0])
                present.append(lst[1])
                percentage.append(PresentageAttendance(rollno, subject))
            except Exception as e:
                print(f"Error processing attendance for {subject}: {e}")
        for subs in ["CT","DST"]:
            lst1=colouratt(PresentageAttendance(rollno, subject))

        return render(request, "skoolie/attendance.html", {
            "DATE" : "Mon, Sept 04",
            "CT_percentage": percentage[0],
            "CT_total": total[0],
            "CT_present": present[0],
            "CT_color": lst1[0],
            "DST_percentage": percentage[1],
            "DST_total": total[1],
            "DST_present": present[1],
            "DST_color": lst1[1],
        })
        

