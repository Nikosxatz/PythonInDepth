sum=0
meg=0
mik=0
for i in range(8):
    a=int(input('Δώσε ηλικία:'))
    sum=sum+a
    if a<=18: 
        mik=mik+1
    elif a>=40:
        meg=meg+1
mo=sum/8
print('Μέσος όρος=',mo)
print('Πλήθος μικρών=',mik)
print('Πλήθος μεγάλων=',meg)










