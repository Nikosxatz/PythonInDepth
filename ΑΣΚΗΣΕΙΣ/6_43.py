import math
NA=math.nan
onomata=['Νίκος','Μιχαήλ','Φωτεινή','Μάνος']
vathmoi=[(9,8,NA,7,4),(9,NA,6,10,6,NA),(8,NA,6),(7,6,6,5,3,7)]
i=0
for o in onomata:
    s=0
    pl=0
    for v in vathmoi[i]:
        if v==v:
            s=s+v
            pl+=1
    mo=s/pl
    print(o,mo)
    i+=1
