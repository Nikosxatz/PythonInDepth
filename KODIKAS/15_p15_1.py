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

class sphere(circle_based_shape):
    def __init__(self,ak,xr):
        super().__init__(ak,xr)

    def emvado(self):
        return 4*self.aktina**2*3.14

    def ogos(self):
        return 4/3*self.aktina**3*3.14


class cylinder(circle_based_shape):
    def __init__(self,ak,yp,xr):
        self.ypsos=yp
        super().__init__(ak,xr)

    def emvado(self):
        return 2*3.14*self.ypsos+2*super().emvado()

    def ogos(self):
        return self.ypsos*super().emvado()


# Κυρίως πρόγραμμα 
ball=sphere(10,'Κόκκινο')
c1=cylinder(5,10,'Πράσινο')
print('Εμβαδό επιφάνειας σφαίρας:',ball.emvado())
print('Όγκος σφαίρας:',ball.ogos())
print('Εμβαδό επιφάνειας κυλίνδρου:',c1.emvado())
print('Όγκος κυλίνδρου:',c1.ogos())
print('Περίμετρος βάσης κυλίνδρου:',c1.perimetros())
ball.scale(2)
print('Όγκος σφαίρας:',ball.ogos())


