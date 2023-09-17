def create_2d_array(grammes,stiles,timi):
    Lst=[]
    for i in range(grammes):
        epipedo2=[]
        for j in range(stiles):
            epipedo2.append(timi)
        Lst.append(epipedo2)
    return Lst


a=create_2d_array(6,6,0)

for i in range(6):
    for j in range(6):
        if i>j:
            a[i][j]=5
        elif i<j:
            a[i][j]=8
        else:
            a[i][j]=i+1
print('==================')

for i in a:
    print(i)
for i in range(6):
    for j in range(6):
        a[i][j],a[j][i]=a[j][i],a[i][j]
print('==================')            

for i in a:
    print(i)
