import math

def melos(n):
    if n==1:
        return 1;
    else:
        res=1/(n*n)+melos(n-1)
        return res

# Κυρίως πρόγραμμα
p=math.sqrt(melos(800)*6)
print(p)






















