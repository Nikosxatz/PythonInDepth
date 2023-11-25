plithos=int(input('Δώσε πλήθος :'))
eidos=input('Δώσε είδος :')
if eidos=='Ε' or eidos=='E':    # Ελληνικό Ε και Λατινικό E
    poso=plithos*0.23
    print('Ποσό:',poso)
elif eidos=='Α' or eidos=='A':  # Ελληνικό Α και Λατινικό A
    poso=plithos*0.70
    print('Ποσό:',poso)
elif eidos=='Τ' or eidos=='T':  # Ελληνικό Τ και Λατινικό T
    poso=plithos*0.15
    print('Ποσό:',poso)
else:
    print('Λάθος είδος')












