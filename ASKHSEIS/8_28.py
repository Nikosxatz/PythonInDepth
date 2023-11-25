def athr_of_tet(f):
    def inner(x,y,z,v):
        return f(x**2, y**2, z**2, v**2)
    return inner

@athr_of_tet
def athr(a,b,c,d):
    return a+b+c+d

# Κυρίως πρόγραμμα
print(athr(1,2,3,4))    



 
