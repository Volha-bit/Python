n = int(input())
total = 0
while n > 0:
    if total == 0 and n < 10:
        break
    total += n % 10
    n //= 10
    if n == 0:
        n, total = total, 0
        continue
print(n)
