def zita_bathmoys():
    b1=float(input('Δώσε 1ο βαθμό:'))
    b2=float(input('Δώσε 2ο βαθμό:'))
    b3=float(input('Δώσε 3ο βαθμό:'))
    t=(b1,b2,b3)
    return t

# Κυρίως πρόγραμμα
b=zita_bathmoys()
mo=(b[0]+b[1]+b[2])/3
print('Ο μέσος όρος είναι ',mo)		












