class oxima:
    def __init__(self,x,e):
        self.xroma=x
        self.etos=e
        
    def info1(self):
        print('Είμαι ένα',self.xroma,'όχημα του',self.etos)
    
class car(oxima):
    def __init__(self,x,e,k,t):
        self.kyvika=k
        self.teliki=t
        super().__init__(x,e)
            
    def info2(self):
        print('Είμαι ένα αυτοκίνητο με',self.kyvika,'κυβικά και',self.teliki,'τελική')  

# Κυρίως πρόγραμμα
c1=car('πράσινο',2018,1800,220)
c1.info2()
c1.info1()




