def protoi():
    n = 1
    while True:
        if n<=3:
            yield n
        else:
            protos=True
            for i in range(2,n//2+1):
                if n%i==0:
                    protos=False
                    break         
            if protos:
                yield n
        n=n+1
                
# Κυρίως πρόγραμμα
for i in protoi():
    print(i)
    if i>50: break
