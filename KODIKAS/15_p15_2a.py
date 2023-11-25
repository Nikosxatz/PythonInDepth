class A:
    pass

class B(A):
    pass

class C(B):
    pass

# Κυρίως πρόγραμμα
print(C.mro())

