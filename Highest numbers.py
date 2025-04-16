# The program is given a number n.
# After the program reads n-numberb and outputs the highest and the second highest.
maxi1 = 0
maxi2 = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a > maxi1:
        maxi2, maxi1 = maxi1, a
    elif a > maxi2:
        maxi2 = a
print(maxi1, maxi2, sep='\n')