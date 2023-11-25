class Lathos(Exception):
    pass

class LathosBathmos(Lathos):
    def __init__(self,bath):
        self.b=bath
    def __str__(self):
        if self.b<0:
            return 'Καλά αρνητικός βαθμός; Ακούς εκεί '+str(self.b)
        else:
            return 'Καλά υπάρχει βαθμός στο πανεπιστήμιο >10;'

class LathosOnoma(Lathos):
    def __init__(self,onom):
        self.o=onom
    def __str__(self):
        if len(self.o)==0:
            return 'Δεν έδωσες τίποτα!!!'       
        elif len(self.o)<3:
            return 'Πολύ μικρό όνομα'
        else:
            return 'Ακους εκεί '+str(len(self.o))+' χαρακτήρες! Κόψε κάτι'

# Κυρίως πρόγραμμα
while True:
    try:
        onoma=input('Δώσε όνομα: ')
        if onoma=='' or len(onoma)>20 or len(onoma)<3:
            raise LathosOnoma(onoma)     
    except LathosOnoma as e1:
        print(e1,'- Δώσε άλλο')                  
    else:
        break

while True:
    try:    
        bathmos=float(input('Δώσε βαθμό :'))
        if bathmos>10 or bathmos<0:
            raise LathosBathmos(bathmos)
    except  LathosBathmos as e1:
        print(e1,'- Δώσε άλλον')                  
    else:
        break
print('Αποδεκτές τιμές !!!')
print('Όνομα  :',onoma)
print('Βαθμός :',bathmos)

