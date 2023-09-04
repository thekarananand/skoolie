import csv
from django.core.files.storage import default_storage
import datetime

def get_greeting():
    current_time = datetime.datetime.now().time()
    
    if current_time.hour < 12:
        return "Good morning"
    elif current_time.hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

# greeting = get_greeting()
# print(greeting)
def colouratt(percent):
    if percent>=75:
        return '#C8FFC8'
    else:
        return '#FFC8C8'
def get_date():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%a, %b %d")
    return formatted_date

def ReadAttendance(rollno, subject):
    total = 0
    present = 0
    absent = 0
    path = f"storage/{subject}.csv"  

    if default_storage.exists(path):
        file_absolute_path = default_storage.path(path)

        with open(file_absolute_path, "r") as obj:
            fobj = csv.reader(obj)
            next(fobj)
            for i in fobj:
                if i[0] == rollno:
                    break

            for j in range(1, 8):
                total = total + 1
                if i[j] == '1':
                    present = present + 1
                if i[j] == '0':
                    absent += 1

            cancel = total - (present + absent)
            track = [total, present, absent, cancel]
            return track
    else:
        # Handle the case where the file doesn't exist
        return None

def PresentageAttendance(rollno, subject):
    track = ReadAttendance(rollno, subject)
    
    if track is not None:
        # Calculate and return the attendance percentage
        return int((track[1] / (track[0] - track[3])) * 100)
    else:
        # Handle the case where the file doesn't exist
        return None
