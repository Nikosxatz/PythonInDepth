class SaravalakiMotors:
    def __init__(self,xr,ek,kv):
        self.xroma=xr
        self.etos_kataskevis=ek
        self.kybika=kv
        self.xiliometra=0
        
    def kornare(self,ar=1):
        for i in range(ar):
            print('Μπίπ',end=' ')
        print()

    def stoixeia(self):
        print('-------------------------')
        print('Χρώμα : ',self.xroma)
        print('Κυβικά :',self.kybika)
        print('Xιλιόμετρα :',self.xiliometra)
        print('Έτος κατασκευής :',self.etos_kataskevis)
        print('-------------------------')

    def ilikia(self,trexon_etos):
        return trexon_etos-self.etos_kataskevis

# Κυρίως πρόγραμμα 
s1=SaravalakiMotors('Κίτρινο',2021,1200)
s2=SaravalakiMotors('Πράσινο',2015,1800)
s1.kornare(3)
s2.stoixeia()
print('Ηλικία :',s2.ilikia(2022))
s1.kornare()
