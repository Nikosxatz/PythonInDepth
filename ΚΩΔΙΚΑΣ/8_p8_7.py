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
for i in fibonacci_numbers():
    print(i)
    if i>100: break


















