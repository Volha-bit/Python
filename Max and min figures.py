# the program calculates the maximum and minimum digits in a given number
a = int(input())
maxi, mini = a % 10, a % 10
a = a // 10
while a != 0:
    if a % 10 < mini:
        mini = a % 10
    if a % 10 > maxi:
        maxi = a % 10
    a = a // 10
print('maximum figure is', maxi)
print('minimum figure is', mini)
