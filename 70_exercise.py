num = int(input("Enter age/year of birth: "))
currentYear = 2022

if num <= currentYear:
    if num <= 100:
        # age
        yearsLeft = 100 - num
        print(f"You will turn 100 years old in {currentYear + yearsLeft}")
    else:
        # year
        currentAge = currentYear - num
        yearsLeft = 100 - currentAge
        print(f"You will turn 100 years old in {currentYear + yearsLeft + 1}")
else:
    print(f"We are still in {currentYear}")

choice = input("Do you want to find your age in a particular year? [y/n]: ")

if "yes" in choice.lower() or "y" in choice.lower():
    year = int(input("Enter that year: "))
    if num <= 100:
        # age
        print(f"Your age in {year} will be {num + (year - currentYear)}")
    else:
        # year
        print(f"Your age in {year} will be {year - num}")
