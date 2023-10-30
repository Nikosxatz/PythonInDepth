class rectangle:
    def __init__(self,a,b,x):
        self.plevra_a=a
        self.plevra_b=b
        self.xroma=x

    def emvado(self):
        return self.plevra_a*self.plevra_b

    def display(self):
        print('Ορθογώνιο ',self.xroma,' ',self.plevra_a,'x',self.plevra_b,' E=',self.emvado()) 

class circle:
    def __init__(self,a,x):
        self.aktina=a
        self.xroma=x

    def emvado(self):
        return 3.14*self.aktina**2

    def display(self):
        print('Κύκλος ',self.xroma,' R=',self.aktina,' E=',self.emvado()) 

# Κυρίως πρόγραμμα 
p1=rectangle(10,5,'Πράσινο')    # Δημιουργία πρώτου ορθογωνίου παραλληλογράμμου με συγκεκριμένες τιμές
p2=rectangle(7,8,'Κόκκινο')     # Δημιουργία δεύτερου ορθογωνίου παραλληλογράμμου με συγκεκριμένες τιμές     
k1=circle(4,'Γαλάζιο')          # Δημιουργία πρώτου κύκλου με συγκεκριμένες τιμές
k2=circle(5,'Κίτρινο')          # Δημιουργία δεύτερου κύκλου με συγκεκριμένες τιμές  
p1.display()                    # Εμφανίζει τα στοιχεία του πρώτου παραλληλογράμμου
k2.display()                    # Εμφανίζει τα στοιχεία του δεύτερου κύκλου
 
