


num1 = num2 = 1
n = int(input())
print(num1, num2, end=' ')
for i in range(2, n):
    num1, num2 = num1, num1 + num2
    print(num2, end=' ')



