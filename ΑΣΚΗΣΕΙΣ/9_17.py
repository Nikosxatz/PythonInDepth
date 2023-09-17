bathmoi=[]
for i in range(10):
    epipedo2=[]
    print('Δώσε βαθμούς για τον φοιτητή Νο'+str(i+1))
    for j in range(3):
        vathmos=float(input('Δώσε τον βαθμό '+str(j+1)+' : '))
        epipedo2.append(vathmos)
    bathmoi.append(epipedo2)
kopikan=0
aristoi=0
for i in range(10):
    s=0
    for j in range(3):
        s=s+bathmoi[i][j]
    mo=s/3
    if mo<5:
        kopikan=kopikan+1
    elif mo>=8.5:
        aristoi=aristoi+1
print('Απέτυχαν',kopikan,' φοιτητές. Ποσοστό',kopikan/10*100,'%')
print('Αρίστευσαν',aristoi,' φοιτητές. Ποσοστό',aristoi/10*100,'%')
