import random

class A:
    def __init__(self):
        self.A1=random.randint(1,1000)

class B(A):
    def __init__(self):
        self.B1=random.randint(1,1000) 

class C(A):
    def __init__(self):
        self.C1=random.randint(1,1000)

class F(B):
    def __init__(self):
        self.F1=random.randint(1,1000)

class D(C):
    def __init__(self):
        self.D1=random.randint(1,1000)

class E(C):
    def __init__(self):
        self.E1=random.randint(1,1000)

