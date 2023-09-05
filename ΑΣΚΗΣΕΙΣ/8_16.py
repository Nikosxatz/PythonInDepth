def mkd(m,n):
    if n>m:
        n,m=m,n
    if n==0: 
        return m
    else: 
        return mkd(n,m%n)
   
# Κυρίως πρόγραμμα
ar1=int(input('Δώσε έναν ακέραιο αριθμό:'))
ar2=int(input('Δώσε και άλλον ακέραιο αριθμό:'))
print('Ο ΜΚΔ του {} και του {} είναι {}'.format(ar1,ar2,mkd(ar1,ar2)))

