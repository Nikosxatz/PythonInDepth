class triangle:
    def __init__(self,b,y):
        self.basi=b
        self.ypsos=y
    def emvado(self):
        return self.basi*self.ypsos/2        
    def show(self):
        print('Β =',self.basi,' Υ =',self.ypsos,' E =',self.emvado())
    def __pow__(self,d):
        self.basi=self.basi**d
        self.ypsos=self.ypsos**d
    def __add__(self,o):
        nb=self.basi-o.basi
        ny=self.ypsos-o.ypsos
        nt=triangle(nb,ny)
        return nt
    def __pos__(self):
        self.basi=self.basi+1
        self.ypsos=self.ypsos+1
  
# Κυρίως πρόγραμμα
t1=triangle(5,10)
t2=triangle(2,4)
t1.show()
+t2
t2.show()
t3=t1+t2
t3.show()
t1**2
t1.show()
