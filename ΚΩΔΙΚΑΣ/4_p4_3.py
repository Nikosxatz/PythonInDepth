timi=float(input('Δώσε τιμή:'))
pos=int(input('Δώσε ποσότητα:'))
pfpa=float(input('Δώσε ποσοστό ΦΠΑ:'))
kostos=timi*pos
fpa=(timi*pos)*pfpa/100
synolo=kostos+fpa
print('Κόστος {:7.2f} x {:2d} -> {:7.2f}€'.format(timi,pos,kostos))
print('ΦΠΑ {:4.1f}%           -> {:7.2f}€'.format(pfpa,fpa))
print('{:23}{}'.format('','========'))
print('{:23}{:7.2f}€'.format('Σύνολο',synolo))







