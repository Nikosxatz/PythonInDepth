plithos=int(input('Δώσε πλήθος πρώτων αριθμών:'))
metritis=0
number=2
while metritis<plithos:
    dieretis=2
    protos=True
    while dieretis<=number//2 and protos==True:
        if number%dieretis==0:
            protos=False
        dieretis+=1
    if protos:
        print(number,end=' ')
        metritis+=1
        if metritis%10==0:print()
    number+=1
    
