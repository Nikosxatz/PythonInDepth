class proion:
    def __init__(self,p,t,a):
        self.perigrafi=p
        self.timi=t
        self.ar=a
    def stoixeia(self):
        print('Έχω',self.ar,self.perigrafi,'με τιμή',self.timi)
    def __imul__(self,a):
        self.ar=self.ar*a
        return self
        
# Κυρίως πρόγραμμα
p1=proion('Καρέκλες',45,4)
p1.stoixeia()
p1*=3
p1.stoixeia()
