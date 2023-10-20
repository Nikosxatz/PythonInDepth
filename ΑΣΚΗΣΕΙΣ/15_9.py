class epiplo:
    def __init__(self,x,v):
        self.xroma=x
        self.varos=v
        
    def info(self):
        print('Χρώμα',self.xroma,'Βάρος',self.varos,'κιλά')
    
class trapezi(epiplo):
    def __init__(self,x,v,p,s):
        self.podia=p
        self.syrtaria=s
        super().__init__(x,v)
            
    def info(self):
        print('Είμαι ένα τραπεζι με',self.podia,'πόδια ',end='')
        if self.syrtaria:
            print('και με συρτάρια')
        else:
            print('χωρίς συρτάρια')
        super().info()
        
# Κυρίως πρόγραμμα
t1=trapezi('Καφέ',50,4,True)
t2=trapezi('Άσπρο',10,3,False)
t1.info()
t2.info()




