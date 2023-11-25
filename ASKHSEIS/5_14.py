theseis=int(input('Δώσε αριθμό θέσεων :'))
epivates=int(input('Δώσε αριθμό επιβατών :'))
pos=epivates*100.0/theseis
if pos>=50:
    print('Κέρδος')
elif pos<30:
    print('Ζημία')


