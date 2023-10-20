class triangle:
    def __init__(self,b,y):
        self.basi=b
        self.ypsos=y
    def emvado(self):
        return self.basi*self.ypsos/2        
    def show(self):
        print('Β =',self.basi,' Υ =',self.ypsos,' E =',self.emvado())
    def __neg__(self):
        self.basi=self.basi*0.9
    def __invert__(self):
        nt=triangle(self.ypsos,self.basi)
        return nt
  
# Κυρίως πρόγραμμα
t1=triangle(5,10)
t1.show()
-t1
t1.show()
t2=~t1
t2.show()

