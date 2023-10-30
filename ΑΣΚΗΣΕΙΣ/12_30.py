class atm:
	def __init__(self,t='χωρίς όνομα',a='πουθενά',p=1000):
		self.trapeza=t
		self.address=a
		self.__poso=p
	def info(self):
		print('Τράπεζα:',self.trapeza) 
		print('Διεύθυνση:',self.address) 
		print('Ποσό:',self.__poso)

# Κυρίως πρόγραμμα
t1=atm('HSBC','ATHENS')
t1.__poso=2000
t1.info()
print(t1.__poso)




