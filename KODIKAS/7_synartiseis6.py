def mesos(b1,b2,b3):
    mo=(b1+b2+b3)/3
    return mo

def apotelesmata(m):
    if m>=8:
        print('Τα πήγες τέλεια',m)
    elif m>=6:
        print('Τα πήγες μέτρια',m)
    elif m>=5:
        print('Πέρασες με',m)
    else:
        print('Δυστυχώς κόπηκες')
        
def info():
    print('==============================')
    print('Τμήμα Πολιτισμικής Τεχνολογίας')
    print('==============================')

def stamata(b1,b2,b3):
    if (b1==0 and b2==0 and b3==0):
        return True
    else:
        return False

# Κυρίως πρόγραμμα
while True:
    a=float(input('Δωσε τον πρώτο βαθμό ->'))
    b=float(input('Δωσε τον δεύτερο βαθμό ->'))
    c=float(input('Δωσε τον τρίτο βαθμό ->'))
    if stamata(a,b,c):
        break
    mm=mesos(a,b,c)
    apotelesmata(mm)
info()













