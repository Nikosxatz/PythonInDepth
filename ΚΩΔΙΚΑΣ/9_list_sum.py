import random
a=[]
sum=0
for i in range(10):
    ar=int(input('Δώσε αριθμό '+str(i+1)+':'))
    a.append(ar)
for i in a:
    sum=sum+i
print('Το άθροισμα των αριθμών που έδωσες είναι ',sum)
