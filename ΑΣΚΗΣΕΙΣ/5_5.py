pos=int(input('Δώσε ποσότητα:'))
timi=float(input('Δώσε τιμή:'))
kostos=timi*pos
if pos>100:
    e=kostos*25/100
    kostos=kostos-e
elif pos>=80 and pos<=100:
    e=kostos*15/100
    kostos=kostos-e
elif pos<20:
    e=kostos*10/100
    kostos=kostos+e
print('Το τελικό κόστος είναι',kostos)





