class SaravalakiMotors:
    def __init__(self,xr,ek):
        self.xroma=xr
        self.etos_kataskevis=ek
        self.__xiliometra=0
        
    def set_xiliometra(self,km):
        self.__xiliometra=km

    def stoixeia(self):
        print('------------------')
        print('Χρώμα : ',self.xroma)
        print('Xιλιόμετρα :',self.__xiliometra)
        print('Έτος :',self.etos_kataskevis)
        print('------------------')

# Κυρίως πρόγραμμα 
s1=SaravalakiMotors('Κίτρινο',2022)
s1.set_xiliometra(55000)
s1.stoixeia()
s1.__xiliometra=10000
s1.stoixeia()
print(s1.__xiliometra)
print(s1._SaravalakiMotors__xiliometra)


