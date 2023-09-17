arithmoi=[]
b=float(input('Δώσε αριθμό : '))
arithmoi.append(b)
for i in range(19):
    b=float(input('Δώσε αριθμό : '))
    if (i>0):
        while True:
            if b>=arithmoi[i-1]:
                arithmoi.append(b)
                break
            else:
                b=float(input('Οπς ... δώσε ξανά αριθμό : '))

print(arithmoi)


    



