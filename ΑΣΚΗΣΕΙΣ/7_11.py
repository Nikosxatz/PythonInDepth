def dms(v,y):
    return v/y**2

def apotelesmata(d):
    if d<=18.5:
        print('Λιποβαρής')
    elif d<=25:
        print('Κανονικός')
    elif d<=30:
        print('Υπέρβαρος')        
    else:
        print('Παχύσαρκος')

# Κυρίως πρόγραμμα
while True:
    varos=float(input('Δώσε βάρος:'))
    if varos==0:
        break
    ypsos=float(input('Δώσε ύψος:'))
    if ypsos==0:
        break
    dd=dms(varos,ypsos)
    apotelesmata(dd)
