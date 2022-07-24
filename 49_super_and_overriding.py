class A:
    var1 = "I am var1 in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"


class B(A):
    var2 = "I am var2 in class B"

    def __init__(self):
        super().__init__()


a = A()
b = B()
