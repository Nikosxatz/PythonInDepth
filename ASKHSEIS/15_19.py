import random

class A:
    def __init__(self):
        self.A1=random.randint(1,1000)
    def display(self):
        print(self.A1)

class B(A):
    def __init__(self):
        self.B1=random.randint(1,1000) 
        super().__init__()
    def display(self):
        print(self.Β1)
        super().display()

class C(A):
    def __init__(self):
        self.C1=random.randint(1,1000)
        super().__init__()
    def display(self):
        print(self.C1)
        super().display()

class F(B):
    def __init__(self):
        self.F1=random.randint(1,1000)
        super().__init__()

    def display(self):
        print(self.F1)
        super().display()

class D(C):
    def __init__(self):
        self.D1=random.randint(1,1000)
        super().__init__()

    def display(self):
        print(self.D1)
        super().display()

class E(C):
    def __init__(self):
        self.E1=random.randint(1,1000)
        super().__init__()

    def display(self):
        print(self.E1)
        super().display()

# Κυρίως πρόγραμμα 
e1=E()
e1.display()

