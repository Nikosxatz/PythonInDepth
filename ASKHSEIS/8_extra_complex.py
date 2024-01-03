'''
	Παραλλαγή της 8_p8_1.py
	Υπολογίζει τις πραγματικές ή τις μιγαδικές ρίζες της εξίσωσης.
	Βλέπε παράγραφο 3.7 του βιβλίου.
	"Παραστάσεις µε µιγαδικούς αριθµούς"
	"Ο τελεστής ανάθεσης και επιστροφής :="
'''
import math
def exisosi(a,b,c):	
	if (d:=b**2-4*a*c) >=0: #Υπολογισμός της Διακρίνουσας και χρήση του warlus operator
		return (-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)			
	else:
		return complex(-b,math.sqrt(-d))/(2*a),complex(-b,-math.sqrt(-d))/(2*a)	

# Κυρίως πρόγραμμα
sa=float(input('Δώσε τον συντελεστή α:'))
sb=float(input('Δώσε τον συντελεστή β:'))
sc=float(input('Δώσε τον συντελεστή γ:'))
riza1,riza2=exisosi(sa,sb,sc)

print('r1={:.4f} r2={:.4f}'.format(riza1,riza2))
























