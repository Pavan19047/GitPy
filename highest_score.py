students = {}

for i in range(3):
    name = input()
    score = int(input())
    students[name] = score

highest_score = None
highest_scorer = None

for student, score in students.items():
    if highest_score is None or score > highest_score:
        highest_score = score
        highest_scorer = student

print({highest_scorer: highest_score})
