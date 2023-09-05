def athr_of_power(f):
    def inner(x,y,z,v,p):
        return f(x**p, y**p, z**p, v**p)
    return inner

@athr_of_power
def athr(a,b,c,d):
    return a+b+c+d

# Κυρίως πρόγραμμα
print(athr(1,2,3,4,10))    



 
