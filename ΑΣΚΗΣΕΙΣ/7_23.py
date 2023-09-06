def test(a):
    global b
    b=8
    a=12
    print(a,b,c)
    return b

def doit(b,a):
    c=15
    b=20
    print(a,b,c)
    a=3
    c=15

# Κυρίως πρόγραμμα
a=4
b=10
c=20
doit(a,b)
c=test(c)
print(a,b,c)
