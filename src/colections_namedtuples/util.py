from collections import namedtuple

def calculate_average_marks(student_num, column_names, student_data):
    Student = namedtuple('Student', column_names)
    info_student = [Student(*data.split()) for data in student_data]
    total_marks = sum(int(student.MARKS) for student in info_student)
    return round(total_marks / student_num, 2)
