# ls = []

# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)

# print(ls)


ls = [i for i in range(100) if i % 3 == 0]
print(ls)

dict1 = {
    i: f"item{i}" for i in range(100)
}

dict2 = {}
for i in range(1, 11):
    dict2[i] = f"item {i}"

print(dict2)

print(dict2)
