def student_averages(subject_scores):
    return [sum(scores) / len(scores) for scores in zip(*subject_scores)]
