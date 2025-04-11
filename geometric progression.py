#The nth term of a geometric progression is found by the formula
#b^n=b^1*q**(n-1)
print('Enter the first element of the progression, the denominator of the progression, and the number of the element being searched.')
b1, q, n = int(input()), int(input()), int(input())
print('The ', n, 'th element is ', b1*q**(n-1), sep='');