import random
Lst=[]
for i in range(5000):
    ar=random.randint(0,36)
    Lst.append(ar)
fores=1
maxfores=0
for i in range(1,5000):
    if Lst[i]==Lst[i-1]:
        fores=fores+1
        if fores>maxfores:
            maxfores=fores
            maxar=Lst[i]
    else:
        fores=1
print(maxfores,maxar)
