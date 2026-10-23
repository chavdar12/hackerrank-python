def run_commands(commands):
    lst, printed = [], []
    for command in commands:
        name, *args = command.split()
        if name == "print":
            printed.append(list(lst))
        else:
            getattr(lst, name)(*map(int, args))
    return printed
