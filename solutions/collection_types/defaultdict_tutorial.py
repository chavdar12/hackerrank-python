from collections import defaultdict


def word_positions(group_a, group_b):
    positions = defaultdict(list)
    for i, word in enumerate(group_a, 1):
        positions[word].append(i)
    return [positions.get(word, [-1]) for word in group_b]
