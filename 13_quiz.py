age = int(input("Enter your age: "))

if age >= 7 and age <= 100:
    if age > 18:
        print("You can drive")
    elif age == 18:
        print("Please visit us")
    elif age < 18:
        print("You can not drive")
else:
    print("Wrong input")
