b1=float(input('Δώσε βαθμό 1ου εξεταστή: '))
b2=float(input('Δώσε βαθμό 2ου εξεταστή: '))
if (b1-b2)>2 or (b2-b1)>2:
    b3=float(input('Δώσε βαθμό 3ου εξεταστή: '))
    d1=b3-b1
    if d1<0:
        d1=-d1
    d2=b3-b2
    if d2<0:
        d2=-d2
    if d1<d2:
        mo=(b3+b1)/2
    else:
        mo=(b3+b2)/2
else:
    mo=(b1+b2)/2
print('Μέσος όρος = ',mo)




