# The asymptotic approximation of a number n is calculated by the formula:
# (1+1/2+1/3+ ... +1/n) - ln(n)
from math import log

n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(total-log(n))
