import csv


CSV_FILE = 'student_data.csv'


def read_student_data():
    with open(CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        student_data = list(reader)
    return student_data


def update_student_data(student_name, subject_name, percentage, subject_names):
    student_data = read_student_data()
    student_data.append({
        'student_name': student_name,
        'subject_name': subject_name,
        'percentage': percentage
    })
    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = ['student_name', 'subject_name', 'percentage']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not student_data:
            writer.writeheader()
        writer.writerows(student_data)


def calculate_attendance_percentage(student_name, subject_names):
    student_data = read_student_data()
    
   
    total_classes = 0
    present_classes = 0
    
    
    for data in student_data:
        if data['student_name'] == student_name and data['subject_name'] in subject_names:
            total_classes += 1
            if float(data['percentage']) > 0:
                present_classes += 1
    
    
    if total_classes > 0:
        attendance_percentage = (present_classes / total_classes) * 100
    else:
        attendance_percentage = 0
    
    return attendance_percentage


