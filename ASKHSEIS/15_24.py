class account:
    def __init__(self,on,p):
        self.onoma=on
        self.poso=p

    def katathesi(self,p):
        self.poso=self.poso+p
        
    def analipsi(self,p):
        self.poso=self.poso-p

    def status(self):
        print('Όνομα:',self.onoma)
        print('Υπόλοιπο:',self.poso)
        
class misthodosia(account):
    def __init__(self,on):
        self.foros=0
        super().__init__(on,0)

    def katathesi(self,p):
        f=p*20/100
        self.foros=self.foros+f
        self.poso=self.poso+p-f

    def analipsi(self,p):
        print('Δεν ειναι δυνατή η ανάληψη από λογαριασμό μισθοδοσίας')

    def status(self):
        super().status()
        print('Φόρος:',self.foros) 

# Κυρίως πρόγραμμα 
m1=misthodosia('Ωνάσης')
m1.katathesi(1000)
m1.status()
m1.katathesi(9000)
m1.status()
m1.katathesi(250)
m1.status()
m1.analipsi(200)

