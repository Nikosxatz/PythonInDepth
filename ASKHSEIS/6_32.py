synolo=0
for i in range(10):
    bathmos=float(input('Δώσε βαθμό:'))
    synolo=synolo+bathmos
    if i==0:
        max1=bathmos
    elif i==1:
        max2=bathmos
        if max1<max2:
            max1,max2=max2,max1
    elif bathmos>max1:
        max2=max1
        max1=bathmos
    elif bathmos>max2:
        max2=bathmos
print(max1,max2,synolo/10)
    
        
    
