class A:
    def __init__(self,n):
        self.name_a=n
        print('Μέθοδος δόμησης κλάσης Α -',self.name_a)

    def meth_a(self):
        print('Μέθοδος βασικής κλάσης A -',self.name_a)

class B(A):
    def meth_b(self):
        print('Μέθοδος παράγωγης κλάσης Β')

obj=B('Νίκος')
print(obj.name_a)
obj.meth_a()
