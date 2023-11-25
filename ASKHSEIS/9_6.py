bathmoi=[]
for i in range(10):
    b=float(input('Δώσε βαθμό : '))
    bathmoi.append(b)
s=0
for i in bathmoi:
    s=s+i
mo=s/10
for i in bathmoi:
    if i>mo:
        print(i)


    



