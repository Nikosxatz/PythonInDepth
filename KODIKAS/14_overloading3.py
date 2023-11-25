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
        pa=self.plevra_a-o.plevra_a
        pb=self.plevra_b-o.plevra_b
        t=rectangle(pa,pb,'Αχρωμο')
        return t

    def __gt__(self, o):
        if self.emvado()<o.emvado():
            return True
        else:
            return False

# Κυρίως πρόγραμμα 
r1=rectangle(10,15,'Πράσινο')    # Δημιουργία πρώτου ορθογωνίου με συγκεκριμένες τιμές
r2=rectangle(4,8,'Κόκκινο')      # Δημιουργία δεύτερου ορθογωνίου με συγκεκριμένες τιμές
r1.display()
r2.display()
n=r1+r2
n.display()
if (r1>r2):
    print('Το',r1.xroma,'ειναι μεγαλύτερο')
else:
    print('Το',r2.xroma,'ειναι μεγαλύτερο')
