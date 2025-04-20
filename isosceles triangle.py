# draw an isosceles triangle of stars with base n
n = int(input())
mid = (n // 2) + 1
for i in range(1, mid):
    print('*' * i)
for i in range(mid, 0, -1):
    print('*' * i)
