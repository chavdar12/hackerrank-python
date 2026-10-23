def happiness(array, liked, disliked):
    return sum((x in liked) - (x in disliked) for x in array)
