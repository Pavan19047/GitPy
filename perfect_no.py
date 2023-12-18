number = int(input())
div_sum = 0
for divisor in range(1, number):
    if number % divisor == 0:
        div_sum += divisor
if div_sum == number:
    print("YES")
else:
    print("NO")
