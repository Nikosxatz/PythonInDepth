class atm:
    def __init__(self,t='χωρίς όνομα',a='πουθενά',p=1000):        
        self.trapeza=t
        self.address=a
        self.__poso=p
	
    def analipsi(self,p):
        self.__poso=self.__poso-p
        
    def katathesi(self,p):    
        self.__poso=self.__poso+p
        
    def ypoloipo(self):    
        return self.__poso    

    def info(self):
        print('Τράπεζα:',self.trapeza) 
        print('Διεύθυνση:',self.address) 
        print('Ποσό:',self.__poso)

    def __del__(self):
        print('Χάθηκαν',self.__poso,' ευρώ')

# Κυρίως πρόγραμμα 
t1=atm('HSBC','ATHENS')
t2=atm()
t2.trapeza='ALPHA'
print(t1.address)
print(t2.ypoloipo())
t1.katathesi(20000)
t1.analipsi(5000)
print(t1.ypoloipo())
t1=t2
print(t1.trapeza)

