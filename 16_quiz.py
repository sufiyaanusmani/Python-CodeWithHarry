items = [int, float, "Harry", 5, 3, 3, 22, 21, 64, 23, 233, 23]

for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)
