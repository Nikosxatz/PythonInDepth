import random
a=[]
for i in range(100):
    a.append(random.randint(1,1000))
zygoi=0
monoi=0
for i in a:
    if i%2==0:
        zygoi=zygoi+i
    else:
        monoi=monoi+i
        
print('Σύνολο ζυγών=',zygoi)
print('Σύνολο μονών=',monoi)
