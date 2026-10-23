def apply_commands(numbers, commands):
    s = set(numbers)
    for command in commands:
        name, *args = command.split()
        getattr(s, name)(*map(int, args))
    return sum(s)
