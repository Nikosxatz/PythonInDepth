class oxima:
    def __init__(self,x,e):
        self.xroma=x
        self.etos=e
        
    def info1(self):
        print('Είμαι ένα',self.xroma,'όχημα του',self.etos)
    
class car(oxima):
    def __init__(self,k,t):
        self.kyvika=k
        self.teliki=t
            
    def info2(self):
        print('Είμαι ένα αυτοκίνητο με',self.kyvika,'κυβικά και',self.teliki,'τελική')  

# Κυρίως πρόγραμμα
c1=car(1200,180)
c1.info2()
#c1.info1()




