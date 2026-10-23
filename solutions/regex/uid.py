def is_valid_uid(uid):
    return (
        len(uid) == 10
        and uid.isalnum()
        and len(set(uid)) == 10
        and sum(c.isupper() for c in uid) >= 2
        and sum(c.isdigit() for c in uid) >= 3
    )
