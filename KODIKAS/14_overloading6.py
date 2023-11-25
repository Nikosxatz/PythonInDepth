class rectangle:
  
    def __init__(self,a,b,x):
        self.plevra_a=a
        self.plevra_b=b
        self.xroma=x

    def emvado(self):
        return self.plevra_a*self.plevra_b

    def display(self):
        print('Ορθογώνιο ',self.xroma,' ',self.plevra_a,'x',self.plevra_b)

    def __len__(self):
        return self.plevra_a*2+self.plevra_b*2

    def __str__(self):
        return 'Ορθογώνιο '+self.xroma+' '+str(self.plevra_a)+'x'+str(self.plevra_b)

    def __bool__(self):
        if self.plevra_a!=0 and self.plevra_b!=0:
            return True
        else:
            return False
       

# Κυρίως πρόγραμμα 
r1=rectangle(10,15,'Πράσινο')    # Δημιουργία πρώτου ορθογωνίου με συγκεκριμένες τιμές
r2=rectangle(4,8,'Κόκκινο')      # Δημιουργία δεύτερου ορθογωνίου με συγκεκριμένες τιμές
r3=rectangle(0,0,'Μαύρο')
r1.display()
r2.display()
print(len(r1))
print(str(r2))
print(bool(r1))
print(bool(r3))
