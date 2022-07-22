import random

lst = ["Snake", "Water", "Gun"]

userWin = 0
botWin = 0

for i in range(0, 5):
    botChoice = random.choice(lst)
    userChoice = input("Enter your choice: ")
    userChoice = userChoice.capitalize()
    print(f"Bot chose {botChoice}")
    if botChoice == "Snake":
        if userChoice == "Snake":
            print("No one wins")
        elif userChoice == "Water":
            print("Bot wins")
            botWin += 1
        elif userChoice == "Gun":
            print("User wins")
            userWin += 1
    elif botChoice == "Water":
        if userChoice == "Snake":
            print("User wins")
            userWin += 1
        elif userChoice == "Water":
            print("No one wins")
        elif userChoice == "Gun":
            print("Bot wins")
            botWin += 1
    elif botChoice == "Gun":
        if userChoice == "Snake":
            print("Bot wins")
            botWin += 1
        elif userChoice == "Water":
            print("User wins")
            userWin += 1
        elif userChoice == "Gun":
            print("No one wins")

print(f"User score: {userWin}")
print(f"Bot score: {botWin}")
