n = int(input())
total = 0   # the sum of its digits
product = 1     # the product of its digits
n_str = str(n)
l = len(n_str)      # the number of digits in it
while n > 0:
    total += n % 10
    product *= n % 10
    n //= 10
arith = total / l   # the arithmetic mean of its digits
print(total, l, product, arith, n_str[0], int(n_str[0]) + int(n_str[-1]), sep='\n')
