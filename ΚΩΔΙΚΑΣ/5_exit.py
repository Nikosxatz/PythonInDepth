import sys
b1=float(input('Δώσε τον πρώτο βαθμό:'))
b2=float(input('Δώσε τον δεύτερο βαθμό:'))
b3=float(input('Δώσε τον τρίτο βαθμό:'))
if b1<0 or b2<0 or b3<0 or b1>10 or b2>10 or b3>10:
   sys.exit()
mesos_oros=(b1+b2+b3)/3
if mesos_oros>=5:
    print('Μπράβο πέρασες')
else:
    print('Δυστυχώς κόπηκες')




