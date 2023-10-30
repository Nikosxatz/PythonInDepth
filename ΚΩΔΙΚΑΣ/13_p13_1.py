import random
        
class circle:
    def __init__(self,a):
        self.aktina=a

    def emvado(self):
        return 3.14*self.aktina**2

    def perimetros(self):
        return 2*3.14*self.aktina

    def display(self):
        print('Κύκλος ακτίνας ',self.aktina,' Εμβαδού',self.emvado(),' Περιμέτρου',self.perimetros()) 

# Κυρίως πρόγραμμα
c=[]
for i in range(10):
    c.append(circle(random.randint(2,20)))

for i in c:
    i.display()
