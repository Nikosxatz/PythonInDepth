class omada:
    def __init__(self,t):
        self.titlos=t
        self.plithos=0
        self.meli=[]
    def info(self):
        print('Ομάδα:',self.titlos,'με',self.plithos,'μέλη')
        for i in range(self.plithos):
            print(self.meli[i])
    def __lshift__(self,f):
        self.meli.append(f)
        self.plithos+=1
    def __add__(self,o):
        nt=omada(self.titlos+'&'+o.titlos)
        nt.plithos=self.plithos+o.plithos
        nt.meli=self.meli+o.meli
        return nt
        
# Κυρίως πρόγραμμα
t1=omada('A1')
t2=omada('B2')
t1<<'Νίκος'
t1<<'Μαρία'
t2<<'Αννα'
t2<<'Τάκης'
t2<<'Κώστας'
t1.info()
t3=t1+t2
t3.info()


