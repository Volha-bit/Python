n = int(input())
a = ''
while n > 0:
    a += str(n % 2)
    n //= 2
print(a[::-1])