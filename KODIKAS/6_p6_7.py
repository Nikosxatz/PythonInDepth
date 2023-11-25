sum=0
ar=int(input('Δώσε αριθμό :'))
for i in range(1,ar//2+1):
    if ar%i==0:
        sum=sum+i
if sum==ar:
    print('Ο αριθμός {} είναι τέλειος'.format(ar))
else:
    print('Ο αριθμός {} δεν είναι τέλειος'.format(ar))


