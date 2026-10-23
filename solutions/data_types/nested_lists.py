def second_lowest_names(students):
    second_lowest = sorted({score for _, score in students})[1]
    return sorted(name for name, score in students if score == second_lowest)
