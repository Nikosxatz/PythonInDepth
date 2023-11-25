synolo=0
for i in range(10):
    poso=float(input('Δώσε ένα ποσό:'))
    if poso<0: continue
    synolo=synolo+poso	
print('Μαζέψαμε συνολικά',synolo,'Ευρώ')
