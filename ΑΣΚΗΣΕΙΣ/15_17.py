class rectangle:
    def __init__(self,a,b,x):
        self.plevra_a=a
        self.plevra_b=b
        self.xroma=x

    def emvado(self):
        return self.plevra_a*self.plevra_b

    def display(self):
        print('Ορθογώνιο ',self.xroma,' ',self.plevra_a,'x',self.plevra_b,' E=',self.emvado())

    def perimetros(self):
        return 2*(self.plevra_a+self.plevra_b)       

class rec3D(rectangle):
    def __init__(self,a,b,c,x):
        self.plevra_c=c
        super().__init__(a,b,x)

    def emvado(self):
        return self.plevra_a*self.plevra_b*2 + self.plevra_a*self.plevra_c*2 + self.plevra_b*self.plevra_c*2

    def ogos(self):
        return self.plevra_a*self.plevra_b*self.plevra_c

    def display(self):
        print('Ορθογώνιο 3D ',self.xroma,' ',self.plevra_a,'x',self.plevra_b,'x',self.plevra_c,'V=',self.ogos())

class cube(rec3D):
    def __init__(self,a,x):
        super().__init__(a,a,a,x)

    def display(self):
        print('Κύβος ',self.xroma,' Πλευράς',self.plevra_a,' Όγκου=',self.ogos())        


class solid_cube(cube):
    def __init__(self,a,x,m):
        self.material=m
        super().__init__(a,x)

    def display(self):
        super().display()
        print('Υλικό :',self.material)
        
# Κυρίως πρόγραμμα 
sc1=solid_cube(10,'Μπλέ','Ξύλο')
sc2=solid_cube(50,'Ροζ','Μάρμαρο')
sc1.display()
sc2.display()
