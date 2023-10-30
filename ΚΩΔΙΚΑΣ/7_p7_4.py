def mesos_oros(bb1,bb2,bb3):
    mm=(bb1+bb2+bb3)/3
    return mm
    
def elegxos_timon(bb1,bb2,bb3):
    if bb1<0 or bb1>10 or bb2<0 or bb2>10 or bb3<0 or bb3>10:
        return False
    else:
        return True

def apotelesma(m):
    if m>=8.5:
        print('Μπράβο άριστα! πήρες ',m)
    elif m>=6.5:
        print('Αρκετά καλά, πέρασες με ',m)
    elif m>=5:
        print('Πέρασες με ',m)
    else:
        print('Δυστυχώς κόπηκες') 
    
# Κεντρική συνάρτηση
def main():
    plithos=0
    synolo=0
    while True:
        b1=float(input('Δώσε 1ο βαθμό:'))
        b2=float(input('Δώσε 2ο βαθμό:'))
        b3=float(input('Δώσε 3ο βαθμό:'))
        if not elegxos_timon(b1,b2,b3):
            break
        plithos+=1
        mo=mesos_oros(b1,b2,b3)
        synolo=synolo+mo
        apotelesma(mo)
    print('=========================')
    if plithos!=0:
        smo=synolo/plithos
        print('Πλήθος φοιτητών:',plithos)
        print('Συνολικός μέσος όρος:',smo)

# Κυρίως πρόγραμμα
main()  # Κλήση της «κεντρικής» συνάρτησης main()


 
