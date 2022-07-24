class Employee:
    """
        Employee Class
    """
    noOfLeaves = 8

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printDetails(self):
        return f"Name is {self.fname}"

    def __add__(self, other):
        return self.fname + " " + other.fname

    def __repr__(self):
        return f"Name is {self.fname}"


# sufiyaan = Employee()
sufiyaan = Employee("Sufiyaan", "Usmani")
harry = Employee("Harry", "Bhai")

print(harry + sufiyaan)
print(sufiyaan)
