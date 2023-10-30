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
for i in range(5):
    for j in range(5-i):
        a[i][j]=1           
for i in a:
    print(i)


