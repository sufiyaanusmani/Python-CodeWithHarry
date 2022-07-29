n = int(input())
ls = []

for i in range(n):
    num = int(input())
    ls.append(num)

newLs = []
for item in ls:
    if item >= 10:
        i = item
        while True:
            i += 1
            if str(i)[::-1] == str(i):
                newLs.append(str(i)[::-1])
                break
    else:
        newLs.append(str(item))


print(newLs)
