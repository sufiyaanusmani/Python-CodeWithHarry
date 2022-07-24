class Employee:
    """
        Employee Class
    """
    noOfLeaves = 8
    _vara = 2   # protected
    __varb = 3  # private

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printDetails(self):
        return f"Name is {self.fname}"

    @classmethod
    def changeLeaves(cls, leaves):
        cls.noOfLeaves = leaves

    @classmethod
    def fromStr(cls, str1):
        params = str1.split(" ")
        return cls(params[0], params[1])

    @staticmethod
    def printGood():
        print("This is good")


class Programmer(Employee):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# sufiyaan = Employee()
sufiyaan = Employee("Sufiyaan", "Usmani")
harry = Employee("Harry", "Bhai")
bill = Employee.fromStr("Bill Gates")

# sufiyaan.name = "Sufiyaan"
# harry.name = "Harry"

sufiyaan.changeLeaves(19)
print(Employee.noOfLeaves)
Employee.changeLeaves(10)
print(Employee.noOfLeaves)

print(sufiyaan.printDetails())
