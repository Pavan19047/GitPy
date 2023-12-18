students = {}

for i in range(3):
    name = input()
    score = int(input())
    students[name] = score


highest_scorer = max(students, key=students.get)

print({highest_scorer: students[highest_scorer]})