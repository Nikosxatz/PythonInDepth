import random

def mysum(Lst,n):
    s=0
    for i in Lst:
        if i>n:
            s=s+i
    return s

a=[]
for i in range(10):
    a.append(random.randint(1,1000))
print(a)
print(mysum(a,500))

