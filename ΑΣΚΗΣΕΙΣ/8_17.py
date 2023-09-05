def mypow(x,y):
    if y==0: 
        return 1
    else:
        return x*mypow(x,y-1)   
   
# Κυρίως πρόγραμμα
ar1=int(input('Δώσε έναν ακέραιο αριθμό:'))
ar2=int(input('Δώσε και άλλον ακέραιο αριθμό:'))
print('Το {} εις την {} είναι {}'.format(ar1,ar2,mypow(ar1,ar2)))

