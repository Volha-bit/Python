n = int(input())
total_digit = 0
product = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        product *= j
    total_digit += product
    product = 1
print(total_digit)