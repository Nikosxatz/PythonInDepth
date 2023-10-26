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
        
class pistotiki(account):
    def __init__(self,on,p,o):
        self.orio=o
        super().__init__(on,p)

    def analipsi(self,p):
        if p>self.orio:
            print('Υπερβήκατε το όριο χρέωσης της κάρτας')
        else:
            self.poso=self.poso-p

# Κυρίως πρόγραμμα 
p1=pistotiki('Μπατίρης',100,50)
p1.katathesi(50)
p1.katathesi(25)
p1.status()
p1.analipsi(20)
p1.analipsi(10)
p1.status()
p1.katathesi(150)
p1.analipsi(70)
p1.status()
