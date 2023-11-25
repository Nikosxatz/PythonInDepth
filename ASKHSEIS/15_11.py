class circle_based_shape:
    def __init__(self,a,x):
        self.aktina=a
        self.xroma=x

    def emvado(self):
        return self.aktina**2 * 3.14
    
    def perimetros(self):
        return 2 * self.aktina * 3.14

    def scale(self,kl):
        self.aktina=self.aktina*kl

class konos(circle_based_shape):
    def __init__(self,ak,y,xr):
        self.ypsos=y
        super().__init__(ak,xr)

    def ogos(self):
        return super().emvado()*self.ypsos/3

# Κυρίως πρόγραμμα 
k=konos(5,10,'Μπλε')
print('Όγκος κώνου:',k.ogos())



