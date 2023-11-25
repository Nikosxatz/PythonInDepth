a=int(input('Δώσε αριθμό:'))
ok=a&128
ar1=(a&120)>>3
ar2=a&7
if ok!=0:
    print('OK')
    print('ar1=',ar1,'ar2=',ar2)
else:
    print('Πρόβλημα!!!')

	














