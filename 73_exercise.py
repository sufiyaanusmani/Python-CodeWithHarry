n = int(input())
ls = []

for i in range(n):
    num = int(input())
    ls.append(num)

for item in ls:
    i = item
    while True:
        i += 1
        if str(i)[::-1] == str(i):
            print(f"Next palindrom for {item} is {i}")
            break
