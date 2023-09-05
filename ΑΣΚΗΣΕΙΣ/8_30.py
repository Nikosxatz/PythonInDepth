def test_type(f):
    def inner(x,y,z,v):
        if (type(x)==int or type(x)==float) and (type(y)==int or type(y)==float) and (type(z)==int or type(z)==float) and (type(v)==int or type(v)==float):
            f(x,y,z,v)
        else:
            print('Που πας βρε Καραμήτρο!')
            return None
    return inner

@test_type
def athr(a,b,c,d):
    return a+b+c+d

# Κυρίως πρόγραμμα
print(athr(1,2,3,4))
print(athr(5,12.2,3.8,4))
print(athr(5,12.2,'A',4))


 
