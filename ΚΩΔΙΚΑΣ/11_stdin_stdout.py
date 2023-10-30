import sys

f1=sys.stdin
f2=sys.stdout
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

