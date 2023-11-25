import random
Lst=[]
for i in range(37):
    Lst.append(0)
for i in range(1000):
    ar=random.randint(0,36)
    Lst[ar]=Lst[ar]+1
print(Lst)
