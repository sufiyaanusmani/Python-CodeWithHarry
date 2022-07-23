class Employee:
    """
        Employee Class
    """
    noOfLeaves = 8

    def __init__(self, name):
        self.name = name

    def printDetails(self):
        return f"Name is {self.name}"

    @classmethod
    def changeLeaves(cls, leaves):
        cls.noOfLeaves = leaves


# sufiyaan = Employee()
sufiyaan = Employee("Sufiyaan")
harry = Employee("Harry")

# sufiyaan.name = "Sufiyaan"
# harry.name = "Harry"

sufiyaan.changeLeaves(19)
print(Employee.noOfLeaves)
Employee.changeLeaves(10)
print(Employee.noOfLeaves)

print(sufiyaan.printDetails())
