from fnmatch import fnmatchcase


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{str(self.fname).lower()}.{str(self.lname).lower()}@python.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return "Email is not set"
        return f"{str(self.fname).lower()}.{str(self.lname).lower()}@python.com"

    @email.setter
    def email(self, s):
        names = s.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


sufiyaan = Employee("Sufiyaan", "Usmani")
harry = Employee("Harry", "Bhai")

print(sufiyaan.explain())
# print(sufiyaan.email)
print(sufiyaan.email)

print(harry.email)
harry.fname = "Haris"
print(harry.email)

harry.email = "cwh.p@python.com"
print(harry.fname)

del harry.email
print(harry.email)
