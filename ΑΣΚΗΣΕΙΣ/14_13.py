class proion:
    def __init__(self,p,t,a):
        self.perigrafi=p
        self.timi=t
        self.ar=a
        self.cnt=0
        
    def stoixeia(self):
        print('Έχω',self.ar,self.perigrafi,'με τιμή',self.timi)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.cnt=self.cnt+1
        if self.cnt>len(self.perigrafi):
            raise StopIteration
        else:
            return self.perigrafi[self.cnt-1]
        
# Κυρίως πρόγραμμα
p1=proion('Καρέκλες',45,4)
p1.stoixeia()
for i in p1:
    print(i)
