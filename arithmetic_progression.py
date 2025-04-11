#arithmetic progression works by the formula: a^n=a^1+d(n-1)
print('Enter the first element of the progression, the difference of the progression, and the number of the element being searched.')
a1, d, n = int(input()), int(input()), int(input())
print('The ', n, 'th element is ', a1+d*(n-1), sep='');