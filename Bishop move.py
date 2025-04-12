#The program accepts coordinates of 2 positions.
#Checks whether the given figure can move from the first position to the second.
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if y2 - y1 == x1 - x2 or y2 - y1 == x2 - x1:
    print('YES')
elif y1 - y2 == x1 - x2 or y1 - y2 == x2 - x1:
    print('YES')
else:
    print('NO');