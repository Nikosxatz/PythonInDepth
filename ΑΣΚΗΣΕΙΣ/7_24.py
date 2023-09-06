def mo():
    m=(a+b+c)/3
    return m

def apotelesma():
    if m>=8.5:
        print('Μπράβο άριστα!')
    elif m>=6.5:
        print('Αρκετά καλά')
    elif m>=5:
        print('Πέρασες')
    else:
        print('Δυστυχώς κόπηκες')

# Κυρίως πρόγραμμα
a=int(input('Δώσε 1ο αριθμό:'))
b=int(input('Δώσε 2ο αριθμό:'))
c=int(input('Δώσε 3ο αριθμό:'))
m=mo()
apotelesma()

