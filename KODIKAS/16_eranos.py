try:
    plithos=int(input('Δώσε πλήθος ατόμων:'))
    if plithos<0:
        raise ValueError
except ValueError:
    plithos=0
i=1
synolo=0
while i<=plithos:
    try: 
        poso=float(input('Δώσε ποσό :'))
        if poso<0:
            raise ValueError
    except ValueError:
        print('Επππ .. αυτή δεν είναι αποδεκτή τιμή - ξαναπροσπάθησε!')
        continue
    else:
        synolo=synolo+poso
        i=i+1      
print('Συνολικό ποσό =',synolo)

