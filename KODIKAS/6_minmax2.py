pl=ar=0
while ar!=9999:
    ar=int(input('Δώσε αριθμό :'))
    if ar!=9999:
        pl=pl+1
        if pl==1:
            max=min=ar
        elif ar>max:
            max=ar
        elif ar<min:
            min=ar
if pl!=0:
    print('max =',max,'min =',min)
else:
    print('Δεν έδωσες κανέναν αριθμό')









