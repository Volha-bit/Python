print("Enter age")
num = int(input())
if num <= 24:
    if num <= 13:
        print("childhood")
    else:
        print("young")
else:
    if num < 60:
        print("adulthood")
    else:
        print("old age")