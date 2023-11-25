class stoixeia:
    def __init__(self):
        self.onoma=''
        self.ilikia=0
        self.varos=0

    def display(self):
        print('Όνομα:',self.onoma)
        print('Ηλικία:',self.ilikia)
        print('Βάρος:',self.varos)
 
# Κυρίως πρόγραμμα 
me=stoixeia()
me.onoma='Νίκος'
me.ilikia=22
me.varos=82
me.display()


