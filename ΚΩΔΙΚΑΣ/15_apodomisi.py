class A:
    def __init__(self,n):
        self.name_a=n
        print('Μέθοδος δόμησης κλάσης Α -',self.name_a)

    def __del__(self):
        print('Μέθοδος αποδόμησης κλάσης Α -',self.name_a)    

    def meth_a(self):
        print('Μέθοδος βασικής κλάσης A')

class B(A):
    def meth_b(self):
        print('Μέθοδος παράγωγης κλάσης Β')

    def __del__(self):
        print('Μέθοδος αποδόμησης κλάσης B')
        super().__del__()

# Κυρίως πρόγραμμα
obj1=B('Νίκος')
obj2=B('Μιχαήλ')
print(obj1.name_a)
del(obj1)
print(obj2.name_a)


