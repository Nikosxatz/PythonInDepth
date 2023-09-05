def athr_of(f):
    def inner(t):
        return [f(i[0],-i[1],i[2],-i[3]) for i in t]
    return inner

@athr_of
def athr(a,b,c,d):
    return a+b+c+d

# Κυρίως πρόγραμμα
print(athr([(8,3,5,5),(6,5,7,9),(10,5,3,1),(6,7,8,2)]))    



 
