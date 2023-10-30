class A:
    def __init__(self,n):
        self.name_a=n
        print('Μέθοδος δόμησης κλάσης Α -',self.name_a)

    def meth_a(self):
        print('Μέθοδος βασικής κλάσης A -',self.name_a)

class B(A):
    def __init__(self,n):
        self.name_b=n
        print('Μέθοδος δόμησης κλάσης B -',self.name_b)
        
    def meth_b(self):
        print('Μέθοδος παράγωγης κλάσης Β -',self.name_b)

obj=B('Νίκος')
obj.meth_a()    # Θα εμφανίσει σφάλμα
obj.meth_b()
