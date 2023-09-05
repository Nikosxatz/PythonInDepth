def perfects():
    num=1
    while True:
        sum=0
        for i in range(1,num//2+1):
            if num%i==0 and i!=num:
                sum=sum+i
        if sum==num:
            yield num
        num=num+1
    
# Κυρίως πρόγραμμα    
p=perfects()
print(next(p))
print(next(p))
print(next(p))
print(next(p))


 
