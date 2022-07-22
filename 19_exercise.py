n = 18
left = 3

while True:
    if left == 0:
        print(f"Game Over, number was {n}")
        break
    else:
        user = int(input(f"Guesses left {left}, Enter your guess: "))
        left -= 1
        if user == n:
            print("Correct")
            break
        elif user > n:
            print("Enter a lower number")
        elif user < n:
            print("Enter a higher number")
