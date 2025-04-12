a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b - coordinates of the king's first position; c, d - coordinates of the king's second position
# Can the king move from the first position to the second position
if (a+1 == c or a-1 ==c) and b == d:
    print('YES')
elif (b+1 == d or b-1 == d) and a == c:
    print('YES')
elif (a+1 == c or a-1 ==c) and b+1 == d:
    print('YES')
elif (a+1 == c or a-1 ==c) and b-1 == d:
    print('YES')
else:
    print("NO")