import random
Lst=[]
for i in range(100):
    Lst.append(random.randint(1,1000))
sum=0
for i in range(100):
    sum=sum+Lst[i]
print(Lst)
print('Το άθροισμα των αριθμών είναι',sum)
found=False
ar=int(input('Δώσε έναν αριθμό :'))
for i in range(100):
    if Lst[i]==ar:
        found=True
        break
if found:
    print('Ο αριθμός',ar,'υπάρχει στη λίστα')
else:
    print('Ο αριθμός',ar,'δεν υπάρχει στη λίστα')


















