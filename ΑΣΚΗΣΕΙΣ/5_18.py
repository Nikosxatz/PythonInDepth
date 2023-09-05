import sys
ar=int(input('Δώσε αριθμό από τη συσκευή:'))
simeio=(ar&240)>>4
alarm=(ar&12)>>2
ok=(ar&2)>>1
if ok==0:
    print('Πρόβλημα στη συσκευή')
    sys.exit()
print('Σημείο ελέγχου:',simeio+1)
if alarm==0: 
    print('OK')
elif alarm==1: 
    print('Φωτιά')
elif alarm==2:
    print('Παραβίαση')
elif alarm==3: 
    print('Καπνός') 
	














