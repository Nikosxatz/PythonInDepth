class proion:
    def __init__(self,p,t,k):
        self.perigrafi=p
        self.timi=t
        self.__kostos=k
        print('Ένα',self.perigrafi,'γεννήθηκε')
    def __kerdos(self):
        return self.timi-self.__kostos    
    def stoixeia(self):
        print('Είμαι ένα',self.perigrafi,'με τιμή',self.timi)

# Κυρίως πρόγραμμα
p1=proion('ρολόι',125,100)
p1.stoixeia()
#print(p1.__kostos)  
#print(p1.__kerdos())  
print('Κόστος =',p1._proion__kostos)  
print('Κέρδος =',p1._proion__kerdos())  
