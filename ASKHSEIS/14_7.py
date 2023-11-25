class proion:
    def __init__(self,p,t,a):
        self.perigrafi=p
        self.timi=t
        self.ar=a
    def stoixeia(self):
        print('Έχω',self.ar,self.perigrafi,'με τιμή',self.timi)
    def __str__(self):
        return self.perigrafi+' '+str(self.ar)
    def __bool__(self):
        if self.timi*self.ar!=0:
            return True
        else:
            return False
        
# Κυρίως πρόγραμμα
p1=proion('Καρέκλες',45,4)
p2=proion('Τραπέζια',100,0)
print(str(p1))
if bool(p2):
    print('Ναι υπάρχει διαθεσιμότητα')
else:
    print('Δεν υπάρχει διαθεσιμότητα ή η αξία είναι μεδενική')
