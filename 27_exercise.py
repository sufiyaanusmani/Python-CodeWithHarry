import datetime
import os


def getDate():
    return datetime.datetime.now()


while True:
    os.system("cls")
    print("Press\n1. Harry\n2. Rohan\n3. Hammad\n\nEnter your choice: ", end="")
    choice1 = int(input())
    if choice1 == 1 or choice1 == 2 or choice1 == 3:
        os.system("cls")
        print("\nPress\n1. Log\n2. View\n\nEnter your choice: ", end="")
        choice2 = int(input())
        os.system("cls")
        if choice1 == 1:
            if choice2 == 1:
                activity = input("Enter activity: ")
                activity = f"[{getDate()}] : {activity}"
                with open("./hms/harry.txt", "at") as f:
                    f.write(f"{activity}\n")
            elif choice2 == 2:
                with open("./hms/harry.txt", "rt") as f:
                    content = f.read()
                    print(content)
                    input("\nPress any key to continue...")
            else:
                print("Wrong choice entered, please enter a valid choice")
        elif choice1 == 2:
            if choice2 == 1:
                activity = input("Enter activity: ")
                activity = f"[{getDate()}] : {activity}"
                with open("./hms/rohan.txt", "at") as f:
                    f.write(f"{activity}\n")
            elif choice2 == 2:
                with open("./hms/rohan.txt", "rt") as f:
                    content = f.read()
                    print(content)
                    input("\nPress any key to continue...")
            else:
                print("Wrong choice entered, please enter a valid choice")
        elif choice1 == 1:
            if choice2 == 1:
                activity = input("Enter activity: ")
                activity = f"[{getDate()}] : {activity}"
                with open("./hms/hammad.txt", "at") as f:
                    f.write(f"{activity}\n")
            elif choice2 == 2:
                with open("./hms/hammad.txt", "rt") as f:
                    content = f.read()
                    print(content)
                    input("\nPress any key to continue...")
            else:
                print("Wrong choice entered, please enter a valid choice")
    else:
        print("Wrong choice entered, enter a valid choice")
