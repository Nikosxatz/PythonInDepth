class A:
    def __init__(self):
        self.AA=1

class B(A):
    def __init__(self):
        self.BB=2
        super().__init__()

class C(A):
    def __init__(self):
        self.CC=3

class D(B):
    def __init__(self):
        self.DD=4
        super().__init__()

# Κυρίως πρόγραμμα 
b1=B()
c1=C()
d1=D()
print(b1.BB)
print(b1.AA)
print(c1.CC)
print(d1.DD)
print(d1.BB)
print(d1.AA)
#print(c1.AA)
