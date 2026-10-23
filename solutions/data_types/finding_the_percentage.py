def average_marks(student_marks, name):
    marks = student_marks[name]
    return "{:.2f}".format(sum(marks) / len(marks))
