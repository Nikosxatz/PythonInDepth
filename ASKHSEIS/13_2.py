import random

class triangle:
    def __init__(self,b,y):
        self.basi=b
        self.ypsos=y
    def emvado(self):
        return self.basi*self.ypsos/2        
    def show(self):
        print('Β =',self.basi,' Υ =',self.ypsos,' E =',self.emvado())
        
# Κυρίως πρόγραμμα
Lst=[]
sum=0
for i in range(10):
    Lst.append(triangle(random.randint(10,100),random.randint(10,100)))
for i in range(10):
    Lst[i].show()
    sum=sum+Lst[i].emvado()            
print('Συνολικό εμβαδό:',sum)




