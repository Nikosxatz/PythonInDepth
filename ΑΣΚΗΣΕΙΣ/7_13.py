def fpa(p,k):
    if k==1:
        return 0
    elif k==2:
        return p*0.06
    elif k==3:
        return p*0.13
    elif k==4:
        return p*0.19
    else:
        return None

# Κυρίως πρόγραμμα
synolo=0
sfpa=0
for i in range(10):
    print('Προιόν Νο',i+1)
    print('===========')
    pl=int(input('Δώσε πλήθος:'))
    timi=float(input('Δώσε τιμή μονάδας:'))
    kfpa=int(input('Δώσε κατηγορία ΦΠΑ (1~4):'))
    axia=pl*timi
    posofpa=fpa(axia,kfpa)
    synolo=synolo+axia
    sfpa=sfpa+posofpa
print('Συνολικό κόστος:',synolo)
print('Συνολικό ΦΠΑ:',sfpa)

