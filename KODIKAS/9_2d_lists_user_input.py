epipedo1=[]
for i in range(3):
    epipedo2=[]
    onoma=input('Δώσε το όνομα του φοιτητή :')
    epipedo2.append(onoma)
    for j in range(3):
        vathmos=float(input('Δώσε τον βαθμό '+str(j+1)+' του '+onoma+':'))
        epipedo2.append(vathmos)
    epipedo1.append(epipedo2)
print(epipedo1)
