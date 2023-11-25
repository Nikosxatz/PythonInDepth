o=input('Δώσε το όνομά σου:')
e=int(input('Δώσε το τρέχον έτος:'))
i=int(input('{} δώσε την ηλικία σου:'.format(o)))
y=float(input('Αρα {} γεννήθηκες το {} δώσε τώρα το ύψος σου:'.format(o,e-i)))
v=float(input('Ωστε έχεις ύψος {}, δώσε και το βάρος σου:'.format(y)))
print('ΔΜΣ={:6.2f}'.format(v/y**2))


