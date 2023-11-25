class oxima:
    def __init__(self,x,e):
        self.xroma=x
        self.etos=e
        
    def info1(self):
        print('Είμαι ένα',self.xroma,'όχημα του',self.etos)
    
class car(oxima):
    def info2(self):
        print('Είμαι ένα αυτοκίνητο')  

# Κυρίως πρόγραμμα
c1=car('κόκκινο',2020)
c1.info1()
c1.info2()



