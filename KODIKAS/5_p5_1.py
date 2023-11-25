# Παράδειγμα Π5.1
import math
a=float(input('Δώσε τον συντελεστή α :'))
b=float(input('Δώσε τον συντελεστή b :'))
c=float(input('Δώσε τον συντελεστή c :'))
d=b**2-4*a*c # Υπολογισμός της διακρίνουσας
if d>0:
    r1=(-b + math.sqrt(d))/(2*a)
    r2=(-b - math.sqrt(d))/(2*a)
    print('Οι ρίζες είναι',r1,'και',r2)
elif d==0:
    r1=-b/(2*a)
    print('Διπλή ρίζα:',r1)
else:
    print('Δεν υπάρχουν πραγματικές ρίζες')




