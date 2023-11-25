import random
    
def suffle(Lst):
    for i in range(2*len(Lst)):
        thesi1=random.randint(0,len(Lst)-1)
        thesi2=random.randint(0,len(Lst)-1)
        Lst[thesi1],Lst[thesi2]=Lst[thesi2],Lst[thesi1]

# Κυρίως πρόγραμμα
a=[11,7,15,6,2,34,23,12,45]
suffle(a)
print(a)
