import math
synolo=0
plithos=0
max=-math.inf
min=math.inf
while synolo<100000:
    poso=float(input('Δώσε ποσό:'))
    plithos+=1
    synolo=synolo+poso
    if poso>max:
        max=poso
    elif poso<min:
        min=poso
print('Σύνολο={} Πλήθος={} Μεγαλύτερο ποσο={} Μικρότερο ποσό={}'.format(synolo,plithos,max,min))















