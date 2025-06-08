from util import calculate_average_marks

if __name__ == '__main__':
    student_num = int(input("Enter number of students: "))
    column_names = input("Enter column names: ").split()
    student_data = [input("Enter student data: ") for _ in range(student_num)]

    avg = calculate_average_marks(student_num, column_names, student_data)
    print("{:.2f}".format(avg))
