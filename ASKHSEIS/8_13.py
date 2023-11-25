def par(n):
    if n==0:
        return 0
    p=n+par(n//2)
    return p

# Κυρίως πρόγραμμα
print(par(20)) 
