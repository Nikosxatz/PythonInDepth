class SaravalakiMotors:
 
    def __init__(self):
        self.xroma=''
        self.etos_kataskevis=0
        self.kybika=1300
        self.xiliometra=0
        
    def kornare(self):
        print('Μπίπ')

    def stoixeia(self):
        print('-------------------------')
        print('Χρώμα : ',self.xroma)
        print('Κυβικά :',self.kybika)
        print('Xιλιόμετρα :',self.xiliometra)
        print('Έτος κατασκευής :',self.etos_kataskevis)
        print('-------------------------')
        
 
# Κυρίως πρόγραμμα 
s1=SaravalakiMotors()
s2=SaravalakiMotors()
s1.xroma='Κόκκινο'
s2.xroma='Μαύρο'
s2.etos_kataskevis=2022
s1.stoixeia()
s1.kornare()
s2.stoixeia()
