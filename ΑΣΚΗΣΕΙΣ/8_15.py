import math

def par(n):
    if n==0:
        return 0
    else:
        p=math.sqrt(2+par(n-1))
    return p

def all(k):
    if k==0:
        return 2
    else:
        p=2/par(k)*all(k-1)
    return p;

# Κυρίως πρόγραμμα
print(all(500)) 
