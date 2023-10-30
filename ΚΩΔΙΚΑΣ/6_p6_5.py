pl_ar=0
pl_ap=0
for i in range(1,11):
    ok=False
    while not ok:
        print('Δώσε βαθμούς για τον {} φοιτητή:'.format(i))
        b1=float(input('Δώσε 1ο βαθμό:'))
        b2=float(input('Δώσε 2ο βαθμό:'))
        b3=float(input('Δώσε 3ο βαθμό:'))
        if b1>=0 and b1<=10 and b2>=0 and b2<=10 and  b3>=0 and b3<=10:
            ok=True
        else:
            print('ΛΑΘΟΣ-αποδεκτοί βαθμοί από 0 μέχρι 10')
            continue
        mo=(b1+b2+b3)/3;
        if mo>=8.5: pl_ar+=1
        if mo<5: pl_ap+=1
print('Πλήθος αριστούχων = ',pl_ar)
print('Πλήθος αποτυχόντων = ',pl_ap)

