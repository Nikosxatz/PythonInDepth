with open('fraseis.txt','w',encoding='utf-8') as f:
    pl=0
    while True:
        frasi=input('Γράψε μια φράση > ')
        if frasi=='':
            break
        if frasi[0].isupper():
            f.write(frasi)
            f.write('\n')
            pl=pl+1
print(pl)
f1=open('num.txt','r')
f2=open('fraseis.txt','a+',encoding='utf-8')
pl=0
sum=0
for i in f1:
    pl=pl+1
    ar=int(i)
    if pl==1:
        mn=ar
        mx=ar
    elif ar>mx:
        mx=ar
    elif ar<mn:
        mn=ar
    sum=sum+ar

mo=sum/pl
f2.write('Πλήθος='+str(pl)+' Μέση τιμή='+str(mo))
f2.write('\nΜέγιστος='+str(mx)+' Ελάχιστος='+str(mn))
f1.close()
f2.close()
        

    
