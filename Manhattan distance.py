# the coordinates of two points are given.
# From the first point we need to get to the second point.
p1, p2, q1, q2 = [int(input()) for i in range(4)]
print(abs(p1 - q1)+abs(p2 - q2))
