# The program outputs:
# -arithmetic mean
# -geometric mean
# -harmonic mean
# -quadratic mean
# of the numbers a and b
import math
a, b = float(input()), float(input())
print((a + b)/2)
print(math.sqrt(a * b))
print((2 * a * b)/(a + b))
print(math.sqrt((pow(a, 2) + pow(b, 2))/2))
