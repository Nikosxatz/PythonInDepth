class A:
    def __init__(self,n):
        self.name_a=n
        print('Μέθοδος δόμησης κλάσης Α -',self.name_a)

    def meth_a(self):
        print('Μέθοδος βασικής κλάσης A -',self.name_a)

class B(A):
    def __init__(self,nb,na):
        self.name_b=nb
        print('Μέθοδος δόμησης κλάσης B -',self.name_b)
        super().__init__(na)

    def meth_b(self):
        print('Μέθοδος παράγωγης κλάσης Β -',self.name_b)

obj=B('Νίκος','Μιχαήλ')
obj.meth_b()
obj.meth_a()
print(obj.name_b)
print(obj.name_a)
