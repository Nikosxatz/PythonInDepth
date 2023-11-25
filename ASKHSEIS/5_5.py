pos=int(input('Δώσε ποσότητα:'))
timi=float(input('Δώσε τιμή:'))
kostos=timi*pos
if pos>100:    
    kostos=0.75*kostos
elif pos>=80 and pos<=100:    
    kostos=0.85*kostos
elif pos<20:    
    kostos=1.10*kostos
print('Το τελικό κόστος είναι',kostos)







