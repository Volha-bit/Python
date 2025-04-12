a, b, c, d = int(input()), int(input()), int(input()), int(input())
mini = 0
if a <= b:
    mini = a
else:
    mini = b
if c < mini:
    mini = c
if d < mini:
    mini = d
print("Minimum number:", mini);