a=float(input('Δωσε τον πρώτο βαθμό ->'))
b=float(input('Δωσε τον δεύτερο βαθμό ->'))
c=float(input('Δωσε τον τρίτο βαθμό ->'))
def mesos(b1,b2,b3):
    mo=(b1+b2+b3)/3
    return mo
mm=mesos(a,b,c)
def apotelesmata(m):
    if m>=8:
        print('Τα πήγες τέλεια',m)
    elif m>=6:
        print('Τα πήγες μέτρια',m)
    elif m>=5:
        print('Πέρασες με',m)
    else:
        print('Δυστυχώς κόπηκες')
apotelesmata(mm)
def info():
    print('==============================')
    print('Τμήμα Πολιτισμικής Τεχνολογίας')
    print('==============================')
info()













