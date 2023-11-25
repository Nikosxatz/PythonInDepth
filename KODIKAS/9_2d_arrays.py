import random
def create_2d_array(grammes,stiles,timi):
    Lst=[]
    for i in range(grammes):
        epipedo2=[]
        for j in range(stiles):
            epipedo2.append(timi)
        Lst.append(epipedo2)
    return Lst

# Κυρίως πρόγραμμα
a=create_2d_array(3,5,0)
for g in a:
    print(g)
for i in range(3):          # Θα μπορούσε να μπει και range(len(a))
    for j in range(5):      # Θα μπορούσε να μπει και range(len(a[0]))
        a[i][j]=random.randint(1,100)
print('---------------------')
for g in a:
    print(g)
