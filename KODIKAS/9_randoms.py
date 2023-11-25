import random
a=[]
for i in range(10):
    a.append(random.randint(1,1000))
for i in range(10):
    if a[i]>500:
        print(a[i])
print('=============')
for i in a:
    if i<100:
        print(i)
