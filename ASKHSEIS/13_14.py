class proion:
    def __init__(self,p,t):
        self.perigrafi=p
        self.timi=t
        print('Ένα',self.perigrafi,'δημιουργήθηκε')
     
    def stoixeia(self):
        print(self.perigrafi,'με τιμή',self.timi)
    
    def set(self,s):
        if type(s) is str:
            self.perigrafi=s
        elif type(s) is int or type(s) is float:
            self.timi=s  

# Κυρίως πρόγραμμα        
p1=proion('πουκάμισο',45)
p1.stoixeia()
p1.set('ρολοι')
p1.stoixeia()
p1.set(200)
p1.stoixeia()



