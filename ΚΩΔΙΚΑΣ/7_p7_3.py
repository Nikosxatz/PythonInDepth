def mesos_oros():
    mm=(b1+b2+b3)/3
    return mm
    
def elegxos_timon():
    if b1<0 or b1>10 or b2<0 or b2>10 or b3<0 or b3>10:
        return False
    else:
        return True

def apotelesma():
    if mo>=8.5:
        print('Μπράβο άριστα! πήρες ',mo)
    elif mo>=6.5:
        print('Αρκετά καλά, πέρασες με ',mo)
    elif mo>=5:
        print('Πέρασες με ',mo)
    else:
        print('Δυστυχώς κόπηκες') 
    
# Κυρίως πρόγραμμα
plithos=0
synolo=0
while True:
    b1=float(input('Δώσε 1ο βαθμό:'))
    b2=float(input('Δώσε 2ο βαθμό:'))
    b3=float(input('Δώσε 3ο βαθμό:'))
    if not elegxos_timon():
        break
    plithos+=1
    mo=mesos_oros()
    synolo=synolo+mo
    apotelesma()
print('=========================')
if plithos!=0:
    smo=synolo/plithos
    print('Πλήθος φοιτητών:',plithos)
    print('Συνολικός μέσος όρος:',smo)


 
