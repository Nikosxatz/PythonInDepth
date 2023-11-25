class S:
    pass

class A(S):
    pass

class B(S):
    pass

class AB(B, A):
    pass

# Κυρίως πρόγραμμα
print(AB.mro())

