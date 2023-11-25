a=int(input('Δώσε την ηλικία σου:'))
f=float(input('Δώσε το ύψος σου:'))
v=float(input('Δώσε το βάρος σου:'))
s=input('Δώσε το όνομά σου:')
print('{:10}{:3d}'.format(s,a))
print('Υψος={:5.2f}   Βάρος={:4.1f}'.format(f,v))
print('ΔΜΣ={:6.3f}'.format(f/v**2))
print(30*s[0])

