import sys
h24=int(input('Δώσε την ώρα σε 24ωρη μορφή: '))
lepta=int(input('Δώσε τα λεπτά: '))
if h24>24 or h24<0 or lepta<0 or lepta>59 or (h24==24 and lepta>0):
    print('Λάθος ώρα')
    sys.exit()
else:
    h12=h24 % 12
    if h12==0:
        h12=12
    if h24==24 or h24<12:
        mor_aft='πμ'
    elif h24>=12:
        mor_aft='μμ'
print('{}:{}{}'.format(h12,lepta,mor_aft))
















