def create_2d_array(grammes,stiles,timi):
    Lst=[]
    for i in range(grammes):
        epipedo2=[]
        for j in range(stiles):
            epipedo2.append(timi)
        Lst.append(epipedo2)
    return Lst

# Κυρίως πρόγραμμα
a=create_2d_array(11,11,0)

for i in range(11):
    while True:
        ap=int(input('Παικτη Νο'+str(i+1)+' ποιόν ψηφίζεις:'))
        if ap==0:
            break
        if ap<0 or ap>11:
            print('##### Δεν υπάρχει τέτοιος παίκτης! #####')
        elif a[i][ap-1]==1:
            print('##### Εχεις ξαναψηφίσει αυτον τον παίκτη! #####')
        else:
            a[i][ap-1]=1
        
print('===============================')

for i in a:
    print(i)
print('===============================')    
eayto=0
for j in range(11):
    s=0
    for i in range(11):
        s=s+a[i][j]
        if i==j and a[i][j]==1:
            eayto=eayto+1    
    print('Παίκτης Νο',j,' Ψήφοι=',s)
print('Ψήφισαν τον εαυτό τους',eayto,'παίκτες')    
