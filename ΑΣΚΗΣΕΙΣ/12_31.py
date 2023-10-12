class atm:
    def __init__(self,t='χωρίς όνομα',a='πουθενά',p=1000):        
        self.trapeza=t
        self._address=a
        self.__poso=p
	
    def __info(self):
        print('Τράπεζα:',self.trapeza) 
        print('Διεύθυνση:',self._address) 
        print('Ποσό:',self.__poso)

# Κυρίως πρόγραμμα 
t1=atm('HSBC','ATHENS',100)
t1.trapeza='ΕΘΝΙΚΗ'
t1._address='ΛΕΣΒΟΣ'
t1._atm__poso=200
t1._atm__info()



