class proion:
    __plithos=0
    def __init__(self,p,t):
        self.perigrafi=p
        self.timi=t
        proion.__plithos+=1
        print('Ένα',self.perigrafi,'δημιουργήθηκε')
     
    def stoixeia(self):
        print(self.perigrafi,'με τιμή',self.timi)

    @classmethod
    def synola(cls):
        print('Σύνολο προϊόντων:',cls.__plithos)
        

# Κυρίως πρόγραμμα        
p1=proion('πουκάμισο',45)
p2=proion('ρολόι',125)
proion.synola()
p1.synola()


