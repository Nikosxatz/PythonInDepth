def test_type(f):
    def inner(x,y,z,v):
        if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float) and  (type(z) is int or type(z) is float) and (type(v) is int or type(v) is float):
            return f(x,y,z,v)
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


 
