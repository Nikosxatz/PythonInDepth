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

    def vale_mpros(self):
        self.doylevei=True
        print('#'+self.xroma+'#','Μπρουμ μπρουμ μπρουμ .... ΟΚ πήρα μπρός!')

    def proxora(self,metra):
        if not self.doylevei:
            print('#'+self.xroma+'#','Δεν προχωράω γιατί είμαι σβηστό!')
            return
        self.xiliometra=self.xiliometra+metra/1000
        print('#'+self.xroma+'#','Προχώρησα',metra,' μέτρα')
        SaravalakiMotors.km_all=SaravalakiMotors.km_all+metra/1000

         
# Κυρίως πρόγραμμα 
s1=SaravalakiMotors('Κίτρινο',2021,1200)
s2=SaravalakiMotors('Πράσινο',2015,1800)
s1.vale_mpros()
s1.proxora(1200)
s1.proxora(2300)
s2.vale_mpros()
s2.proxora(1500)
print('Σύνολο χιλιομέτρων από s2 :',s2.km_all)
print('Σύνολο χιλιομέτρων από κλάση :',SaravalakiMotors.km_all)
s2.km_all=0
print('==================================')
print('Σύνολο χιλιομέτρων από κλάση:',SaravalakiMotors.km_all)
print('Σύνολο χιλιομέτρων από s2:',s2.km_all)
print('Σύνολο χιλιομέτρων από s1:',s1.km_all)
