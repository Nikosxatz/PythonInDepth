from math import sqrt

a=float(input('Δώσε τον συντελεστή a:'))
b=float(input('Δώσε τον συντελεστή b:'))
c=float(input('Δώσε τον συντελεστή c:'))
d=b**2-4*a*c # Υπολογισμός της διακρίνουσας
r1=(-b + sqrt(d))/(2*a)
r2=(-b - sqrt(d))/(2*a)
print('Οι ρίζες είναι',r1,'και',r2)


