# # Pattern Printing
# Input = Integer n
# Boolean = True or False

# True:
# *
# **
# ***
# ****

# False:
# ****
# ***
# **
# *

n = int(input("Enter number of rows: "))
b = True
b = int(input("Enter 1 for True or 0 for false: "))

if b == 0:
    b = False

if b == True:
    for i in range(0, n):
        print("*" * (i+1))
else:
    for i in range(n, 0, -1):
        print("*" * i)
