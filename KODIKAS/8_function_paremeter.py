def gin(a,b):
    g=a*b
    return g

def test(s):
    a=int(input('a='))
    b=int(input('b='))
    t=s(a,b)
    print(t)
  
# Κυρίως πρόγραμμα
test(gin)
f=gin
test(f)






















