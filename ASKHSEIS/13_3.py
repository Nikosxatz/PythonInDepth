class proion:
    plithos=0
    def __init__(self,p,t):
        self.perigrafi=p
        self.timi=t
        proion.plithos+=1
        print('Ένα',self.perigrafi,'δημιουργήθηκε')
     
    def stoixeia(self):
        print(self.perigrafi,'με τιμή',self.timi)

# Κυρίως πρόγραμμα        
p1=proion('πουκάμισο',45)
p2=proion('ρολόι',125)
print(p1.plithos)
print(p2.plithos)
print(proion.plithos)


