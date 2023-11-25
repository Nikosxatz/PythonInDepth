class point:
    def __init__(self,xp,yp):
        self.x=xp
        self.y=yp

    def info(self):
        print('Σημείο ',self.x,',',self.y)

    def to_str(self):
        return 'Σημείο '+str(self.x)+','+str(self.y)
    

class polyline:
    def __init__(self,x_start,y_start,x_end,y_end):
        self.start=point(x_start,y_start)
        self.end=point(x_end,y_end)
        self.shmeia=[self.start,self.end]

    def neo_shmeio(self,x,y):
        self.shmeia.append(point(x,y))

    def info(self):
        print('Γραμμή με',len(self.shmeia),' σημεια:')
        for s in self.shmeia:
            s.info()
        
# Κυρίως πρόγραμμα        
g1=polyline(10,20,40,50)
g1.info()
g1.neo_shmeio(100,200)
g1.neo_shmeio(400,50)
g1.info()




