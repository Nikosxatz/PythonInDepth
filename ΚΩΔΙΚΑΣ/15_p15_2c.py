class S:
    pass

class A:
    pass

class B(S):
    pass

class AB(B, A):
    pass

# Κυρίως πρόγραμμα
print(AB.mro())

