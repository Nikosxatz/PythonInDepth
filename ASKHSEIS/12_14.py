class rectangle:
    def __init__(self,a,b,x):
        self.pa=a
        self.pb=b
        self.xr=x
        print('Ένα',self.xr,'ορθογώνιο δημιουργήθηκε')
    def perimetros(self):
        return 2*self.pa+2*self.pb
    def set(self,a,b):
        if a>0 and b>0:
            self.pa=a
            self.pb=b
        else:
            self.pa=0
            self.pb=0
    def display(self):
        print('Ορθογώνιο ',self.xr,' ',self.pa,'x',self.pb)


# Κυρίως πρόγραμμα
r1=rectangle(5,10,'κόκκινο')
r2=rectangle(15,20,'πράσινο')
r1.display()
print(r2.perimetros())
r1.set(3,7)
r1.display()
r2.set(3,-4)
r2.display()
