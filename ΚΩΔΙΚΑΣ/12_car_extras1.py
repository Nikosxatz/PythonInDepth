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
s3=SaravalakiMotors('Black',2004,1500)
s1.kotsadoros='Auto Hak'
s2.fortistis='Black & Decker'
print(s1.kotsadoros)
print(s2.fortistis)
#print(s3.kotsadoros)    # Το s3 δεν έχει μέλος kotsadoros
#print(s1.fortistis)     # Το s1 δεν έχει μέλος fortistis    


