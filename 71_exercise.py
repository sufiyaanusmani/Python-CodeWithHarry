n = int(input("Enter number of apples: "))
mn = int(input("Enter minimum number of students: "))
mx = int(input("Enter maximum number of students: "))

for i in range(mn, mx+1):
    if n % i == 0:
        print(f"{i} is a divisor of {n}")
    else:
        print(f"{i} is not a divisor of {n}")
