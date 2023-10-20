class proion:
    def __init__(self,p,t,a):
        self.perigrafi=p
        self.timi=t
        self.ar=a
    def stoixeia(self):
        print('Έχω',self.ar,self.perigrafi,'με τιμή',self.timi)
    def __eq__(self,o):
        if type(o) is proion:
            if self.timi==o.timi and self.perigrafi==o.perigrafi:
                return True
            else:
                return False
        elif type(o) is int or type(o)is float:
            if self.timi*self.ar==o:
                return True
            else:
                return False        
        elif type(o) is str:
            if self.perigrafi==o:
                return True
            else:
                return False    
        elif type(o) is list:
            return self.timi*self.ar-o[0]*o[1]
        else:
            print('Λάθος')
            return None
        
# Κυρίως πρόγραμμα
p1=proion('Καρέκλες',45,4)
p2=proion('Τραπέζια',100,2)
print(p1==p2)
print(p2==200)
print(p1=='Καρέκλες')
print(p2==[3,60])
print(p1==(1,2))
