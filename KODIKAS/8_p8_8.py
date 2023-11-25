def fibonacci_numbers():
    f1=0
    yield f1  
    f2=1
    yield f2 
    while True:
        f3=f1+f2
        yield f3        
        f1=f2
        f2=f3  
        
# Κυρίως πρόγραμμα
f=fibonacci_numbers()
for i in range(10):
    print(next(f))
print(f.__next__())
print(f.__next__())
    



















