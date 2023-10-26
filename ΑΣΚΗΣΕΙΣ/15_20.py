class A:
    def __init__(self):
        print('Class A')

class B:
    def __init__(self):
        print('Class B')

class C(A,B):
    def __init__(self):
        print('Class C')
        super().__init__()

class D(C):
    def __init__(self):
        print('Class D')
        super().__init__()

class E(C):
    def __init__(self):
        print('Class E')
        super().__init__()

# Κυρίως πρόγραμμα 
c1=C()
d1=D()

