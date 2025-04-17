# The program is given a number n. The program outputs the first n numbers of the Fibonacci sequence
n = int(input())
num1 = 1
num2 = 0
for _ in range(n):
    print(num1, end=' ')
    num1, num2 = num1+num2, num1
