b1=float(input('Δώσε βαθμό 1ου εξεταστή: '))
b2=float(input('Δώσε βαθμό 2ου εξεταστή: '))
if abs(b1-b2)>2: # Βλέπε συνάρτηση abs() στο κεφάλαιο 3  
    b3=float(input('Δώσε βαθμό 3ου εξεταστή: '))
    d1=abs(b3-b1)  
    d2=abs(b3-b2)    
    if d1<d2:
        mo=(b3+b1)/2
    else:
        mo=(b3+b2)/2
else:
    mo=(b1+b2)/2
print('Μέσος όρος = ',mo)




