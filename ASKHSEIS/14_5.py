class triangle:
    def __init__(self,b,y):
        self.basi=b
        self.ypsos=y
    def emvado(self):
        return self.basi*self.ypsos/2        
    def show(self):
        print('Β =',self.basi,' Υ =',self.ypsos,' E =',self.emvado())
    def __rshift__(self,o):
        o.basi=self.basi
        o.ypsos=self.ypsos
  
# Κυρίως πρόγραμμα
t1=triangle(5,10)
t2=triangle(20,50)
t2.show()
t1>>t2
t2.show()

