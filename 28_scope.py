# l = 10      # Global


# def function1(n):
#     l = 5   # Local
#     print(l)
#     print(n)


# function1(11)
# print(l)


l = 10      # Global


def function1(n):
    global l   # Global
    l = l + 45
    print(l)
    print(n)


function1(11)
print(l)
