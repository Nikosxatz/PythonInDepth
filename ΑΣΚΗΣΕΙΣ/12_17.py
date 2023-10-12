class stoixeia:
    def __init__(self,o='',i=0,v=0):
        self.onoma=o
        self.ilikia=i
        self.varos=v
    def set(self,o,i,v):
        self.onoma=o
        self.ilikia=i
        self.varos=v
    def display(self):
        print('Όνομα:',self.onoma)
        print('Ηλικία:',self.ilikia)
        print('Βάρος:',self.varos)
    
# Κυρίως πρόγραμμα
me=stoixeia('Νίκος',22,82)
me.display()
me.set('Μιχαήλ',5,19)
me.display()


