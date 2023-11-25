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


# Κυρίως πρόγραμμα 
r1=rec3D(10,20,30,'Κόκκινο')
r1.display()
print(r1.emvado())
print(r1.ogos())
print(r1.perimetros())
