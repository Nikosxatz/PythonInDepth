class rectangle:
    def __init__(self,a,b,x):
        self.plevra_a=a
        self.plevra_b=b
        self.xroma=x
    def emvado(self):
        return self.plevra_a*self.plevra_b
    def perimetros(self):
        return 2*(self.plevra_a+self.plevra_b)
    def display(self):
        print(self.xroma,' ',self.plevra_a,'x',self.plevra_b)
    def __eq__(self,o):
        if type(o) is rectangle:
            if self.emvado()==o.emvado():
                return True
            else:
                return False
        elif type(o) is circle:
            if self.xroma==o.xroma:
                return True
            else:
                return False
    def __invert__(self):
        self.plevra_a,self.plevra_b=self.plevra_b,self.plevra_a
     

class circle:
    def __init__(self,a,x):
        self.aktina=a
        self.xroma=x
    def emvado(self):
        return 3.14*self.aktina**2
    def perimetros(self):
        return 2*3.14*self.aktina
    def display(self):
        print(self.xroma,' R=',self.aktina)
    def __mul__(self,o):
        self.aktina= self.aktina*o
    def __add__(self,o):
        if type(o) is circle:
            ak=self.aktina+o.aktina
            xr='Αχρωμο'
            c=circle(ak,'Αχρωμο')
            return c            
        elif type(o) is rectangle:
            em=self.emvado()+o.emvado()
            per=self.perimetros()+o.perimetros()
            if self.xroma!=o.xroma:
                xr=self.xroma+'+'+o.xroma
            else:
                xr=self.xroma
            s=sxima(em,per,xr)
            return s

class sxima:
    def __init__(self,e,p,x):
        self.emvado=e
        self.perimetros=p
        self.xroma=x
    def info(self):
        print('Χρώμα σχήματος :',self.xroma)
        print('Εμβαδό σχήματος :',self.emvado)
        print('Περίμετρος σχήματος :',self.perimetros)
    def __len__(self):
        return self.perimetros
    def __str__(self):
       return 'Σχήμα '+self.xroma

# Κυρίως πρόγραμμα
r1=rectangle(4,8,'Κόκκινο')
r2=rectangle(5,10,'Πράσινο')
~r2
r2.display()
if r1==r2:
    print('Ισα ορθογώνια')
else:
    print('Άνισα ορθογώνια')
c1=circle(20,'Πράσινο')
c1*2
c1.display()
n=c1+r1
if r2==c1:
    print('Το ορθογώνιo και ο κύκλος είναι ίδια')
else:
    print('Ορθογώνιο και κύκλος δεν είναι ίδια')
print(str(n))
