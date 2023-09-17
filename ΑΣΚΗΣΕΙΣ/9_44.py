def doit(size):
    Lst=[]
    for i in range(size):
        epipedo2=[]
        for j in range(size):
            epipedo2.append(0)
        Lst.append(epipedo2)
    
    arxi=0
    telos=size-1
    while arxi<=telos:
        for i in range(arxi,telos+1):
            Lst[arxi][i]=arxi+1
        for i in range(arxi,telos+1):
            Lst[telos][i]=arxi+1    
        for i in range(arxi,telos+1):
            Lst[i][arxi]=arxi+1
        for i in range(arxi,telos+1):
            Lst[i][telos]=arxi+1    
        arxi=arxi+1
        telos=telos-1
    return Lst

# Κυρίως πρόγραμμα
s=int(input('Δώσε μέγεθος πίνακα:'))
a=doit(s)
for i in a:
    print(i)
