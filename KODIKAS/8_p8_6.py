def apot(k,l,f):
    a=f(k,l)
    print('Αποτέλεσμα =',a)
    
# Κυρίως πρόγραμμα
x=int(input('Δώσε έναν αριθμό:'))
y=int(input('Δώσε ακόμη έναν αριθμό:'))
g=lambda x,y:x*y
apot(x,y,g)
apot(x,y,lambda x,y:x+y)






















