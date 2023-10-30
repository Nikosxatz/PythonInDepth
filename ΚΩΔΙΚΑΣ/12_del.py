class proion:
    def __init__(self,p,t):
        self.perigrafi=p
        self.timi=t
        print('Ένα',self.perigrafi,'γεννήθηκε')
    def stoixeia(self):
        print('Είμαι ένα',self.perigrafi,'με τιμή',self.timi)
    def __del__(self):
        print('Το',self.perigrafi,'μας άφησε χρόνους')

def test():
    p3=proion('ποδήλατο',250)
    
# Κυρίως πρόγραμμα
p1=proion('πουκάμισο',45)
p2=proion('ρολόι',125)
test()
del p2
p1=12  


