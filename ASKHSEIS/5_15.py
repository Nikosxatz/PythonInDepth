milia=float(input('Δώσε μίλια :'))
litra=float(input('Δώσε λίτρα :'))
kat=litra/milia		
if kat<=0.9:
    print('Πολύ χαμηλή')
elif kat<=1.2:
    print('Χαμηλή')
elif kat<=1.8:
    print('Κανονική')
else:
    print('Υψηλή')



