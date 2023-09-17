def compare(v):
    return max(v[1:])

# Κυρίως πρόγραμμα
voles=[]        
for i in range(3):
    epipedo2=[]
    o=input('Δώσε όνομα αθλητή : ')
    epipedo2.append(o)
    for j in range(6):
        v=float(input('Δώσε βολή Νο '+str(j+1)+' : '))
        epipedo2.append(v)
    voles.append(epipedo2)
    
voles.sort(reverse=True,key=compare)
for i in voles:
    print(i[0],max(i[1:]))


