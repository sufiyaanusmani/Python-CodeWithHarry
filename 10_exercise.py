# Create a dictionary and take input from the user and return the meaning of the word from the dictionary

course = {
    "oop": "Object Oriented Programming",
    "dld": "Digital Logic Design",
    "pf": "Programming Fundamentals",
    "la": "Linear Algebra"
}

str1 = input("Enter course: ")
str1 = str1.lower()

if str1 in course:
    print(course[str1])
else:
    print("Not found")
