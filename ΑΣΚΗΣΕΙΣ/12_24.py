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
at1=atm()
at1.trapeza='ALPHA'

#print(at1.__poso)  # η μεταβλητή-μέλος __poso δεν είναι άμεσα προσβάσιμη γιατί θεωρείται «ιδιωτική»
at1._atm__poso=100
at1.info()
print(at1.ypoloipo())
at3=atm('ΠΕΙΡΑΙΩΣ','ΑΘΗΝΑ',2000)
at3.info()
at4=atm()
at4.info()
at5=atm('ΕΘΝΙΚΗ')
at3.info()
at6=atm(p=200)
at6.info()
at1.katathesi(1000)
at1.analipsi(500)
at1.info()
del at1


