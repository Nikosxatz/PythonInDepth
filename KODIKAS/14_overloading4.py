class rectangle:
  
    def __init__(self,a,b,x):
        self.plevra_a=a
        self.plevra_b=b
        self.xroma=x

    def emvado(self):
        return self.plevra_a*self.plevra_b

    def display(self):
        print('Ορθογώνιο ',self.xroma,' ',self.plevra_a,'x',self.plevra_b)

    def __pos__(self):
        self.plevra_a=self.plevra_a*1.2
        self.plevra_b=self.plevra_b*1.2

    def __neg__(self):
        pa=self.plevra_a*0.8
        pb=self.plevra_b*0.8
        t=rectangle(pa,pb,'Μαύρο')
        return t

# Κυρίως πρόγραμμα 
r1=rectangle(10,15,'Πράσινο')    # Δημιουργία πρώτου ορθογωνίου με συγκεκριμένες τιμές
r2=rectangle(4,8,'Κόκκινο')      # Δημιουργία δεύτερου ορθογωνίου με συγκεκριμένες τιμές
r1.display()
r2.display()
+r1
r1.display()
n=-r2
n.display()
