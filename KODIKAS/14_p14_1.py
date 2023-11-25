class proion:
    def __init__(self,p,t,a):
        self.perigrafi=p
        self.timi=t
        self.ar=a
    def stoixeia(self):
        print('Έχω',self.ar,self.perigrafi,'με τιμή',self.timi)
    def __add__(self,o):
        if self.perigrafi==o.perigrafi:
            nt=(self.timi*self.ar+o.timi*o.ar)/(self.ar+o.ar)
            nar=self.ar+o.ar
            n=proion(self.perigrafi,nt,nar)
            return n
        else:
            print('Δεν μπορω να προσθέσω ανόμοια προϊόντα')            
            return None
    def __lt__(self,o):
        if self.timi*self.ar<o.timi*o.ar:
            return True
        else:                     
            return False
    def __eq__(self,o):
        if self.timi*self.ar==o.timi*o.ar:
            return True
        else:                     
            return False
    def __pos__(self):
        self.timi=self.timi*1.1
  
# Κυρίως πρόγραμμα
p1=proion('πουκάμισα',45,3)
p2=proion('ρολόγια',125,7)
p3=proion('πουκάμισα',80,5)
p4=p1+p3
p4.stoixeia()
+p2
p2.stoixeia()
if p1<p3:
    print('Τα ',p1.perigrafi,' έχουν μικρότερη αξία')
elif p1==p2:
    print('Τα έχουν ίδια αξία')
else:
    print('Τα ',p3.perigrafi,' έχουν μικρότερη αξία')


