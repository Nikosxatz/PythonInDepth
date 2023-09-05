import sys
h24=int(input('Δώσε την ώρα σε 24ωρη μορφή: '))
lepta=int(input('Δώσε τα λεπτά: '))
if h24>23 or h24<0 or lepta<0 or lepta>59:
    print('Λάθος ώρα')
    sys.exit()
if h24>=12:
    h12=h24-12
    if h12==0:
        h12=12
    print('{}:{}μμ'.format(h12,lepta))		
else:
    if h24==0:
        h12=12
    else:
        h12=h24
    print('{}:{}πμ'.format(h12,lepta))	














