# An n number is fed to the program. The program outputs the n-th number in the Fibonacci sequence
n = int(input())
num1 = 1
num2 = 1
for _ in range(3, n+1):
    num1, num2 = num1 + num2, num1
print(num1)