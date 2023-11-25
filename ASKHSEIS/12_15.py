class circle:
    def __init__(self,a,x):
        self.aktina=a
        self.xroma=x
    def perimetros(self):
        return 2*3.14*self.aktina
    def display(self):
        print('Κύκλος με περίμετρο',self.perimetros())    

# Κυρίως πρόγραμμα
c1=circle(100,'μπλε')
c2=circle(30,'κόκκινο')
print(c2.perimetros())
c1.display()

