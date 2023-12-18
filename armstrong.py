num = int(input())
s_num = str(num)
power = len(s_num)
final_ans = 0

for i in s_num:
    final_ans += pow(int(i),power)
if final_ans == num:
    print("YES")
else:
    print("NO")