import random
xreoseis=[]
hmeres_mina=(31,28,31,30,31,30,31,31,30,31,30,31)
mines=('Ιανουάριος','Φεβρουάριος','Μάρτιος','Απρίλιος','Μαϊος','Ιούνιος','Ιούλιος','Αυγουστος','Σεπτέμβριος','Οκτώβριος','Νοέμβριος','Δεκέμβριος')
for i in range(12):
    epipedo2=[]
    print()
    print('***** Χρεώσεις για μήνα : ',mines[i],' *****')
    for j in range(hmeres_mina[i]):
        xr=float(input('Δώσε χρέωση ημερομηνίας '+str(j+1)+'/'+mines[i]+' :'))
        epipedo2.append(xr)
    xreoseis.append(epipedo2)

mx=xreoseis[0][0]
for i in xreoseis:
    for j in i:
        if j>mx:
            mx=j

print('Ημερομηνία/ες με τη μέγιστη χρέωση',mx)
for i in range(12):
    for j in range(hmeres_mina[i]):
        if xreoseis[i][j]==mx:
            print(j+1,mines[i])
