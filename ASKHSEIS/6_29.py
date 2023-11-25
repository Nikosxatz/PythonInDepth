poso=float(input('Δωσε αρχικό ποσό διδάκτρων:'))
et=int(input('Δώσε πλήθος ετών υπολογισμού:'))
for i in range(1,et+1):
    print('Ποσό {}ου έτους:{}'.format(i,poso))
    poso=poso+poso*7/100

