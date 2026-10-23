def captains_room(k, rooms):
    return (k * sum(set(rooms)) - sum(rooms)) // (k - 1)
