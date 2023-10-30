def is_perfect(num):
    sum=0
    for i in range(1,num//2+1):
        if num%i==0:
            sum=sum+i
    if sum==num:
        return True
    else:
        return False
    
# Κυρίως πρόγραμμα    
apo=int(input('Από αριθμό:'))
eos=int(input('Έως αριθμό:'))        
for i in range(apo,eos+1):
    if is_perfect(i):
        print(i)





 
