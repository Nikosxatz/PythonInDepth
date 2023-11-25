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
        if type(o) is rectangle:
            pa=self.plevra_a+o.plevra_a
            pb=self.plevra_b+o.plevra_b
            t=rectangle(pa,pb,'Αχρωμο')
            return t
        elif type(o) is int or type(o) is float:
            pa=self.plevra_a+o
            pb=self.plevra_b+o
            t=rectangle(pa,pb,'Μαύρο')
            return t

    def __gt__(self, o):
        if type(o) is rectangle:
            if self.emvado()>o.emvado():
                return True
            else:
                return False
        elif type(o) is int or type(o) is float:
            if self.emvado()>o:
                return True
            else:
                return False

# Κυρίως πρόγραμμα 
r1=rectangle(10,3,'Πράσινο')    # Δημιουργία ορθογωνίου με συγκεκριμένες τιμές
r1.display()
n=r1+5
n.display()
e=float(input('Δώσε τιμή σύγκρισης :'))
if (r1>e):
    print('Είναι μεγαλύτερο από',e)
else:
    print('Δεν είναι μεγαλύτερο από',e)
