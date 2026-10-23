def merge_the_tools(string, k):
    return ["".join(dict.fromkeys(string[i:i + k])) for i in range(0, len(string), k)]
