def par(n):
    if n==1:
        return 1
    else:
        p=1/n+par(n-1)
    return p
   
# Κυρίως πρόγραμμα
ar=int(input('Δώσε έναν ακέραιο αριθμό:'))
print('Το άθροισμα της σειράς για n={} είναι {}'.format(ar,par(ar)))

