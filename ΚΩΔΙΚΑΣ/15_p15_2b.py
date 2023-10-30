class A:
    pass

class B:
    pass

class AB(B, A):
    pass

# Κυρίως πρόγραμμα
print(AB.mro())

