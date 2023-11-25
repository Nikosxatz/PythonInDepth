class rectangle:
    plithos=0
    def __init__(self,a,b,x):
        self.plevra_a=a
        self.plevra_b=b
        self.xroma=x
        rectangle.plithos=rectangle.plithos+1

    def emvado(self):
        return self.plevra_a*self.plevra_b

    def display(self):
        print(self.xroma,' ',self.plevra_a,'x',self.plevra_b,' E=',self.emvado()) 

    @classmethod
    def synola(cls):
        print('Σύνολο ορθογωνίων =',cls.plithos)

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

    @classmethod
    def synola(cls):
        print('Σύνολο ορθογωνίων 3D=',cls.plithos)

# Κυρίως πρόγραμμα 
r1=rec3D(10,20,30,'Κόκκινο')
r2=rec3D(5,15,40,'Πράσινο')
print('Πλήθος=',r2.plithos)
print(rec3D.plithos)
rec3D.synola()

