class boats:
    def __init__(self,on,mik):
        self.onoma=on
        self.mikos=mik

    def display(self):
        print('Όνομα:',self.onoma)
        print('Μήκος:',self.mikos)
    
class foyskoto(boats):
    def __init__(self,on,mik,thal):
        self.thalamoi=thal
        super().__init__(on,mik)

    def display(self):
        super().display()
        print('Αεροθάλαμοι:',self.thalamoi)

# Κυρίως πρόγραμμα 
f1=foyskoto('Skipper',7.80,7)
f2=foyskoto('Planatech',5.70,5)
f1.display()
f2.display()



