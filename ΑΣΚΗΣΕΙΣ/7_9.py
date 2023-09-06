def pi():
    s=1
    for i in range(2,2000,2):
        s=s*i**2/((i-1)*(i+1))
    return s*2
    
# κυρίως πρόγραμμα
print('Πι=',pi())
   



 
