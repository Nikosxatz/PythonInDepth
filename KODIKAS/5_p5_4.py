eis=float(input('Δωσε το εισόδημά σου:'))
if eis<=5000:
    foros=0
elif eis<=15000:
    foros=(eis-5000)*10/100
elif eis<=30000:
    foros=10000*10/100+(eis-15000)*25/100
else:
    foros=10000*10/100+15000*25/100+(eis-35000)*35/100
print('Ο φόρος για εισόδημα',eis,'είναι',foros)


