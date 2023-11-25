class proion:
    plithos=0
    def __init__(self,p,t):
        self.perigrafi=p
        self.timi=t
        proion.plithos+=1
        print('Ένα',self.perigrafi,'δημιουργήθηκε')

# Κυρίως πρόγραμμα        
p1=proion('πουκάμισο',45)
p2=proion('ρολόι',125)
p1.plithos=12
print(p2.plithos)
print(p1.plithos)
print(proion.plithos)
proion.plithos=44
print(p2.plithos)




