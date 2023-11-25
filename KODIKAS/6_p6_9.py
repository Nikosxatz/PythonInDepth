import math
NA=math.nan
sum=0
n=0
d=0
times=[12.6,17,18,NA,23,24.5,NA,19,NA,14]
for t in times:
    if t==t:
        sum=sum+t
        n=n+1
    else:
        d=d+1
mo=sum/n
print('Μέση θερμοκρασία',mo)
print('Προσοχή',d,'αισθητήρες δεν λειτουργούν')
    
