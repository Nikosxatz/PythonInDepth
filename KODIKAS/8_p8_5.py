def gin(a,b):
    g=a*b
    return g

def sum(a,b):
    s=a+b
    return s

def apot(k,l,f):
    a=f(k,l)
    print('Αποτέλεσμα =',a)
    
# Κυρίως πρόγραμμα
x=int(input('Δώσε έναν αριθμό:'))
y=int(input('Δώσε ακόμη έναν αριθμό:'))
apot(x,y,gin)
apot(x,y,sum)






















