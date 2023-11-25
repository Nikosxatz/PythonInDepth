ar=int(input('Δώσε έναν ακέραιο αριθμό:'))
z=m=0
while ar!=0:
    if ar%2==0:
        z+=1
    else:
        m+=1
    ar=int(input('Δώσε έναν ακέραιο αριθμό:'))
print(z,m)


    
