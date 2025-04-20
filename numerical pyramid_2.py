n = int(input())
for i in range(1, n + 1):
    m = 1
    for j in range(i):
        print(m, end='')
        m += 1
    m -= 2
    for j in range(i, 1, -1):
        print(m, end='')
        m -= 1
    print()