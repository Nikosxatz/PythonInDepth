import random
a=[]
for i in range(100):
    a.append(random.randint(0,2000))
mx=a[0]
thesi=0
for i in range(100):
    if a[i]>mx:
        mx=a[i]
        thesi=i
print(mx,thesi)


    



