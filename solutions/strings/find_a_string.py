def count_substring(string, sub_string):
    return sum(string.startswith(sub_string, i) for i in range(len(string)))
