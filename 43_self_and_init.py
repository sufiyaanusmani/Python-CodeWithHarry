class Employee:
    """
        Employee Class
    """
    noOfLeaves = 8

    def __init__(self, name):
        self.name = name

    def printDetails(self):
        return f"Name is {self.name}"


# sufiyaan = Employee()
sufiyaan = Employee("Sufiyaan")
harry = Employee("Harry")

# sufiyaan.name = "Sufiyaan"
# harry.name = "Harry"


print(sufiyaan.printDetails())
