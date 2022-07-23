# def function1():
#     print("Subscribe Now")


# func2 = function1


# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum


# a = funcret(1)
# print(a)


# def executor(func):
#     func("this")


# executor(print)

def dec1(func1):
    def now1():
        print("Executing now")
        func1()
        print("Executed")
    return now1


@dec1
def whoami():
    print("Sufiyaan Usmani")


whoami()
