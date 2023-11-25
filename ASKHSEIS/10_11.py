etos=input('Δώσε διψήφιο έτος π.χ. 22,23 κλπ > ')
ctlist=['ct'+etos+str(ct).zfill(3) for ct in range(1,101)]
foitites=dict.fromkeys(ctlist,'------')
ar=0
for k in foitites.keys():
    onom=input('Δώσε όνομα για τον κωδικό '+k+' > ')
    if onom=='':
        break
    foitites.update({k:onom})
    ar=ar+1
print(ar,' Φοιτητές:')
for o in foitites.values():  
    if o!='------':
        print(o)
    

