students = {}
for i in range(3):
    s_name = input()
    score = input()
    students[s_name] = score

highest_scorer = highest_score = None

for student, score in students.items():
    if highest_score == None or score > highest_score:
        highest_score = score
        highest_scorer = student
highest_score_data = {highest_scorer: highest_score}
print(highest_score_data)
