class A:
    def meth1(self):
        print('Μέθοδος1 κλάσης Α')

    def meth2(self):
        print('Μέθοδος2 κλάσης Α')

class B:
    def meth1(self):
        print('Μέθοδος1 κλάσης B')

    def alli(self):
        print('Άλλη μέθοδος  κλάσης Β')

class AB(A,B):
    def meth2(self):
        print('Μέθοδος2 κλάσης AB')    

    def meth3(self):
        print('Μέθοδος3 κλάσης AB')  

# Κυρίως πρόγραμμα 
obj=AB()
obj.meth2()
obj.meth3()
obj.alli()
obj.meth1()
print(AB.mro())
