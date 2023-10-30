b1=float(input('Δώσε τον πρώτο βαθμό:'))
b2=float(input('Δώσε τον δεύτερο βαθμό:'))
b3=float(input('Δώσε τον τρίτο βαθμό:'))
b4=float(input('Δώσε τον τέταρτο βαθμό:'))
if b1>=b2 and b1>=b3 and b1>=b4:
    print('Ο μεγαλύτερος είναι ο',b1)
elif b2>=b1 and b2>=b3 and b2>=b4:
    print('Ο μεγαλύτερος είναι ο',b2)
elif b3>=b1 and b3>=b2 and b3>=b4:
    print('Ο μεγαλύτερος είναι ο',b3)
else:
    print('Ο μεγαλύτερος είναι ο',b4)
if b1<=b2 and b1<=b3 and b1<=b4:
    print('Ο μικρότερος είναι ο',b1)
elif b2<=b1 and b2<=b3 and b2<=b4:
    print('Ο μικρότερος είναι ο',b2)
elif b3<=b1 and b3<=b2 and b3<=b4:
    print('Ο μικρότερος είναι ο',b3)
else:
    print('Ο μικρότερος είναι ο',b4)




