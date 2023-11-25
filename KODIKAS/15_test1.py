class A:
    def meth_a(self):
        print('Μέθοδος βασικής κλάσης A')

class B(A):
    def meth_b(self):
        print('Μέθοδος παράγωγης κλάσης Β')

obj=B()
obj.meth_b()
obj.meth_a()
