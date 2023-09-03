import csv
def attendance(roll_no):
    with open('CT.csv', 'r') as file:
            reader = csv.DictReader(file)
            student_data = list(reader)

            for row in student_data:
             if row['Roll No'] == roll_no:
                
                attendance_values = [int(row[f'Subject{i}']) for i in range(1, 6)]

                # Calculate attendance percentage
                attendance_percentage = attendance_percentage(attendance_values)
                return attendance_percentage

             return None

def attendance_percentage(attendance_values):
    total_classes = len(attendance_values)
    present_classes = attendance_values.count(1)
    no_class = attendance_values.count(-1)

    if total_classes == 0:
        return 0.0 

    
    attendance_percentage = (present_classes / (total_classes - no_class)) * 100.0

    return attendance_percentage