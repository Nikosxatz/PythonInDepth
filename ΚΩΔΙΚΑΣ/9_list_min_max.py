import random
a=[]
for i in range(10):
    a.append(random.randint(1,1000))
min=a[0]
max=a[0]
for i in range(10):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]
print('Μέγιστος=',max,'Ελάχιστος=',min)

