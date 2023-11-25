import math
min=math.inf
max=-math.inf
for i in range(1,11):
    ar=float(input('Δώσε έναν αριθμό:'))
    if ar>max:
        max=ar
    elif ar<min:
        min=ar
print('max=',max,'min=',min)










