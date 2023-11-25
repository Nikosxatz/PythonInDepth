found=False
ar=int(input('Δώσε αριθμό :'))
for i in range(2,ar//2+1):
    if ar%i==0: found=True
if found:
    print('Ο αριθμός {} δεν είναι πρώτος'.format(ar))
else:
    print('Ο αριθμός {} είναι πρώτος'.format(ar))


