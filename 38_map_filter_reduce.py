# numbers = ["2", "34", "64"]

# # Map
# numbers = list(map(int, numbers))


# def sq(a):
#     return a*a


# # map(what function you want to perform on each element, name of the list)

# # num = [2, 3, 4, 5, 6, 77, 77]
# # square = list(map(sq, num))
# # print(square)

# # num = [2, 3, 4, 5, 6, 77, 77]
# # square = list(map(lambda x: x*x, num))
# # print(square)

# def square(a):
#     return a*a


# def cube(a):
#     return a*a*a


# func = [square, cube]
# num = [2, 3, 4, 5, 6, 77, 77]
# for i in range(5):
#     val = list(map(lambda x: x(i), func))
#     print(val)


# # Filter
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def isGreater5(num):
#     return num > 5


# grThan5 = list(filter(isGreater5, list1))
# print(grThan5)


# Reduce
from functools import reduce

list1 = [1, 2, 3, 4]
prod = reduce(lambda x, y: x+y, list1)
print(prod)
