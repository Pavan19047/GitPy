word = input()
student_dict = {}
for i in word:
    if i.isalpha():
        student_dict[i] = word.count(i)
print(student_dict)
