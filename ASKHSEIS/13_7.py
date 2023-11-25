class point:
    def __init__(self,xp,yp):
        self.x=xp
        self.y=yp

    def info(self):
        print('Σημείο ',self.x,',',self.y)

    def to_str(self):
        return 'Σημείο '+str(self.x)+','+str(self.y)
    

class line:
    def __init__(self,x_start,y_start,x_end,y_end):
        self.start=point(x_start,y_start)
        self.end=point(x_end,y_end)

    def info(self):
        print('Γραμή απο',self.start.to_str(),'μέχρι',self.end.to_str())
        
# Κυρίως πρόγραμμα        
g1=line(10,20,40,50)
g1.info()
p1=point(100,200)
p1.info()



