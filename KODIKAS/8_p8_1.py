import math
def exisosi(a,b,c):
	d=b**2-4*a*c # Υπολογισμός της διακρίνουσας
	if d>0:
		r1=(-b+math.sqrt(d))/(2*a)
		r2=(-b-math.sqrt(d))/(2*a)
	elif d==0:
		r1=r2=-b/(2*a)
	else:
		r1=r2=None
	return r1,r2

# Κυρίως πρόγραμμα
sa=float(input('Δώσε τον συντελεστή α:'))
sb=float(input('Δώσε τον συντελεστή β:'))
sc=float(input('Δώσε τον συντελεστή γ:'))
riza1,riza2=exisosi(sa,sb,sc)
if riza1!=None:
	print('r1=',riza1,' r2=',riza2)
else:
	print('Η εξίσωση δεν έχει πραγματικές ρίζες')























