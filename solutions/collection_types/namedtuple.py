from collections import namedtuple


def average_marks(columns, rows):
    Student = namedtuple("Student", columns)
    marks = [int(Student._make(row).MARKS) for row in rows]
    return "{:.2f}".format(sum(marks) / len(marks))
