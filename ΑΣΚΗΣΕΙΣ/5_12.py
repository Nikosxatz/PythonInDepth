plithos=int(input('Δώσε πλήθος :'))
eidos=input('Δώσε είδος :')
if eidos=='E' or eidos=='Ε':
    poso=plithos*0.23
    print('Ποσό:',poso)
elif eidos=='A' or eidos=='Α':
    poso=plithos*0.70
    print('Ποσό:',poso)
elif eidos=='T' or eidos=='Τ':
    poso=plithos*0.15
    print('Ποσό:',poso)
else:
    print('Λάθος είδος')












