ar=int(input('Δώσε αριθμό από τη συσκευή:'))
ok=(ar&128)>>7
eidos=(ar&96)>>5
timi=ar&31;
if ok==1:
    print('Είδος=',eidos,' Τιμή=',timi)
else:
    print('Υπάρχει πρόβλημα στη συσκευή')







