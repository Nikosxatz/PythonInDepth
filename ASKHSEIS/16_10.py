class Lathos(Exception):
    pass

class LathosBathmos(Lathos):
    pass

class LathosOnoma(Lathos):
    pass

# Κυρίως πρόγραμμα
while True:
    try:
        onoma=input('Δώσε όνομα: ')
        if onoma=='':
            raise LathosOnoma('Δεν έδωσες τιποτα για όνομα!')
        if len(onoma)>20 or len(onoma)<3:
            raise LathosOnoma('Πολύ μεγάλο ή μικρό όνομα')
    except LathosOnoma as e1:
        print(e1,'- Δώσε άλλο')                  
    else:
        break

while True:
    try:    
        bathmos=float(input('Δώσε βαθμό :'))
        if bathmos>10 or bathmos<0:
            raise LathosBathmos('Μη επιτρεπτός βαθμός')
    except  LathosBathmos as e1:
        print(e1,'- Δώσε άλλον')                  
    else:
        break
print('Αποδεκτές τιμές !!!')
print('Όνομα  :',onoma)
print('Βαθμός :',bathmos)

