def create_2d_array(grammes,stiles,timi):
    Lst=[]
    for i in range(grammes):
        epipedo2=[]
        for j in range(stiles):
            epipedo2.append(timi)
        Lst.append(epipedo2)
    return Lst            

# Κυρίως πρόγραμμα
a=create_2d_array(6,6,0)
for i in a:
    print(i)
for i in range(6):
    for j in range(6):
        if i+j>5:
            a[i][j]=1
        elif i+j<5:
            a[i][j]=2
        else:
            a[i][j]=0
print('==================')            
for i in a:
    print(i)
