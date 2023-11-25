class proion:
    def __init__(self,p,t,a):
        self.perigrafi=p
        self.timi=t
        self.ar=a
    def stoixeia(self):
        print('Έχω',self.ar,self.perigrafi,'με τιμή',self.timi)
    def __gt__(self,o):
        if self.timi>o.timi:
            return True
        else:
            return False
    def __lshift__(self,o):
        self.timi=o
        
# Κυρίως πρόγραμμα
p1=proion('Καρέκλες',45,4)
p2=proion('Τραπέζια',100,2)
if p2>p1:
    print('Το ',p2.perigrafi,' είναι πιο ακριβό')
else:
    print('Το ',p1.perigrafi,' είναι πιο ακριβό')    
p2<<150
p2.stoixeia()
