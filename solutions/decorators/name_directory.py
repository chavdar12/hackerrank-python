def get_age(person):
    return int(person[2])


def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=get_age)]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
