# a = input("What is your name: ")
# b = input("How much do you earn: ")

# if int(b) == 0:
#     raise ZeroDivisionError("b can not be 0")

# if a.isnumeric():
#     raise Exception("Numbers are not allowed")

# print(f"Hi {a}")


c = input("Enter your name: ")
try:
    print(a)
except Exception as e:
    if c == "harry":
        raise ValueError("Blocked")

    print("variable is not defined")
