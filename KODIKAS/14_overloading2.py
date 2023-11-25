class rectangle:
  
    def __init__(self,a,b,x):
        self.plevra_a=a
        self.plevra_b=b
        self.xroma=x

    def emvado(self):
        return self.plevra_a*self.plevra_b

    def display(self):
        print('Ορθογώνιο ',self.xroma,' ',self.plevra_a,'x',self.plevra_b)

    def __add__(self, o):
        return self.emvado()+o.emvado()

    def __gt__(self, o):
        per1=2*self.plevra_a+2*self.plevra_b
        per2=2*o.plevra_a+2*o.plevra_b
        if per1>per2:
            return self
        else:
            return o

# Κυρίως πρόγραμμα 
r1=rectangle(10,3,'Πράσινο')    # Δημιουργία πρώτου ορθογωνίου με συγκεκριμένες τιμές
r2=rectangle(4,8,'Κόκκινο')     # Δημιουργία δεύτερου ορθογωνίου με συγκεκριμένες τιμές
r1.display()
r2.display()
e=r1+r2
print(e)
max=r1>r2
max.display()

