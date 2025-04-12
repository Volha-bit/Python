#The program accepts coordinates of 2 positions.
#Checks whether the given figure can move from the first position to the second.
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if (y1 + 2 == y2 and (x1 + 1 == x2 or x1 - 1 == x2)) or (y1 - 2 == y2 and (x1+1 == x2 or x1 - 1 == x2)):
    print('YES')
elif (x1 - 2 == x2 and (y1 + 1 == y2 or y1 - 1 == y2)) or (x1 + 2 == x2 and (y1 + 1 == y2 or y1 - 1 == y2)):
    print('YES')
else:
    print('NO');