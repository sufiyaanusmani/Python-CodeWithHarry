# 45 * 3 = 555
# 46 + 9 = 77
# 56 / 6 = 4

op = input("Enter operator: ")
validOp = ["+", "-", "/", "*"]

if op in validOp:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 == 45 and num2 == 3 and op == "*":
        print(555)
    elif num1 == 46 and num2 == 9 and op == "+":
        print(77)
    elif num1 == 56 and num2 == 6 and op == "/":
        print(4)
    else:
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
else:
    print("Invalid Operator")
