from util import calculate_student_average
if __name__ == '__main__':
    n = int(input("Enter number of students: "))
    student_marks = {}

    for _ in range(n):
        name, *line = input("Enter student name and marks: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter query student name: ")
    average = calculate_student_average(student_marks, query_name)
    print("{:.2f}".format(average))
