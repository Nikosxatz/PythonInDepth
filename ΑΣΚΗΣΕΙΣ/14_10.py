class triangle:
    def __init__(self,b,y):
        self.basi=b
        self.ypsos=y
    def emvado(self):
        return self.basi*self.ypsos/2        
    def show(self):
        print('Β =',self.basi,' Υ =',self.ypsos,' E =',self.emvado())
    def __ge__(self,o):
        if type(o) is triangle:
            if self.emvado()>=o.emvado():
                return True
            else:
                return False
        elif type(o) is int or type(o) is float:
            if self.emvado()>=o:
                return True
            else:
                return False
        elif type(o) is tuple:
            if self.basi>=o[0] and self.ypsos>=o[1]:
                return True
            else:
                return False         
        else:
            return None
        
# Κυρίως πρόγραμμα
t1=triangle(5,10)
t2=triangle(7,8)
print(t1>=t2)
print(t1>=20)
print(t1>=(6,10))
print(t1>='test')



