def par(n):
    if n<=0:
        return 0
    p=n+par(n-0.1)
    return p

# Κυρίως πρόγραμμα
print(par(1000)) 
