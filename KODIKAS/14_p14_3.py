class fibonacci: 
    def __init__(self): 
        self.a = 0 
        self.b = 1
        self.oros=0
    def __next__(self):
        if self.oros==0:
            self.oros=self.oros+1
            return 0
        elif self.oros==1:
            self.oros=self.oros+1
            return 1        
        else:
            n=self.a+self.b
            self.a = self.b
            self.b = n
            return n 
    def __iter__(self): 
        return self 

f=fibonacci() 
for i in f:
    print(i,end=' ')
    if i>100:
        break

