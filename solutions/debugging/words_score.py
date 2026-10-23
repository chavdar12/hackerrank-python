def score_words(words, vowels="aeiouy"):
    return sum(1 if sum(c in vowels for c in word) % 2 else 2 for word in words)
