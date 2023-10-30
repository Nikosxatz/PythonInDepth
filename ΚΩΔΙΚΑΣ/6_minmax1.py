for i in range(1,11):
    ar=float(input('Δώσε έναν αριθμό:'))
    if i==1:
        min=max=ar
    elif ar>max:
        max=ar
    elif ar<min:
        min=ar
print('max=',max,'min=',min)









