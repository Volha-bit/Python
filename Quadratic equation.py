# The program looks for roots of the quadratic equation a^2+b*x+c=0
import math

a, b, c = [float(input()) for i in range(3)]
D = pow(b, 2) - 4 * a * c
if D < 0:
    print('no roots')
elif D == 0:
    print(-b / (2 * a))
else:
    print(min((-b - math.sqrt(D)) / (2 * a), (-b + math.sqrt(D)) / (2 * a)))
    print(max((-b - math.sqrt(D)) / (2 * a), (-b + math.sqrt(D)) / (2 * a)))
