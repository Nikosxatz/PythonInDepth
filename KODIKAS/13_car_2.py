class SaravalakiMotors:
    tilefono='2104567893'
    polis='ΑΘΗΝΑ'
    plithos=0
    km_all=0
    
    def __init__(self,xr,ek,kv):
        self.xroma=xr
        self.etos_kataskevis=ek
        self.kybika=kv
        self.xiliometra=0
        self.doylevei=False
        SaravalakiMotors.plithos=SaravalakiMotors.plithos+1
        
    def kornare(self,ar=1):
        print('#'+self.xroma+'#',end=' ')
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

    def frenare(self):
        print('#'+self.xroma+'#','Οοοοοοπς σταμάτησα!')

    def vale_mpros(self):
        self.doylevei=True
        print('#'+self.xroma+'#','Μπρουμ μπρουμ μπρουμ .... ΟΚ πήρα μπρός!')

    def svise(self):
        self.doylevei=False
        print('#'+self.xroma+'#','Τσαφ ... μόλις έσβησα!')
        
    def proxora(self,metra):
        if not self.doylevei:
            print('#'+self.xroma+'#','Δεν προχωράω γιατί είμαι σβηστό!')
            return
        self.xiliometra=self.xiliometra+metra/1000
        print('#'+self.xroma+'#','Προχώρησα',metra,' μέτρα')
        SaravalakiMotors.km_all=SaravalakiMotors.km_all+metra/1000

    def stripse_dexia(self):
        if not self.doylevei:
            print('#'+self.xroma+'#','Δεν στρίβω γιατί είμαι σβηστό!')
            return   
        print('#'+self.xroma+'#','OK έστριψα δεξιά')
        
    def stripse_aristera(self):
        if not self.doylevei:
            print('#'+self.xroma+'#','Δεν στρίβω γιατί είμαι σβηστό!')
            return   
        print('#'+self.xroma+'#','OK έστριψα αριστερά')

    @classmethod
    def etaireia(cls):
        print('Τηλέφωνο :',cls.tilefono)
        print('Πόλις :',cls.polis)
        print('Χιλιόμετρα :',cls.km_all)
        print('Σαραβαλάκια :',cls.plithos)

# Κυρίως πρόγραμμα 
s1=SaravalakiMotors('Κίτρινο',2021,1200)
s2=SaravalakiMotors('Πράσινο',2015,1800)
s1.vale_mpros()
s1.proxora(1200)
s1.stripse_dexia()
s1.proxora(2300)
s1.stoixeia()
s2.vale_mpros()
s2.proxora(1500)
s2.stoixeia()
print('Σύλολο χιλιομέτρων από όλα :',s2.km_all)
print('Σύλολο χιλιομέτρων από όλα :',SaravalakiMotors.km_all)
print('Πλήθος οχημάτων :',SaravalakiMotors.plithos)
SaravalakiMotors.etaireia()
s2.etaireia()



