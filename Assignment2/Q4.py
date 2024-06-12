import numpy as np
scores = [
[80, 90, 70, 85, 95],
[75, 85, 95, 70, 80],
[85, 95, 75, 80, 90],
[90, 80, 85, 75, 70]
]
scores = np.array(scores)

# (A)
average = np.mean(scores, axis=0)
print(f"Average score for each subject: {average}")

# (B)
studentAverageScore = np.mean(scores, axis=1)
highestScore = np.argmax(studentAverageScore)
print(f"The student with highest average score: Student {highestScore+1}")

# (C)
lowest_score_subject = np.argmin(scores[highestScore])
print(f"The subject in which the highest-scoring student has scored the lowest is: Subject {lowest_score_subject+1}")