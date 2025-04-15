# The program is fed the amount to be paid.
# You can use an unlimited number of 25, 10, 5, 1 coins.
# It is necessary to pay the amount with the minimum number of coins.
a = int(input())    # the amount to be paid
counter = 0    # coin counter
while a // 25 >= 1:
    counter += a // 25
    a -= (a // 25)*25
while a // 10 >= 1:
    counter += a // 10
    a -= (a // 10)*10
while a // 5 >= 1:
    counter += a // 5
    a -= (a // 5)*5
while a >= 1:
    counter += a
    a = 0
print(counter)
