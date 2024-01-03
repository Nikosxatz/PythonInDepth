# υπολογισμός αθροίσματος
def add(x,y):
	ss=x+y		# στη μεταβλητή ss ανατίθεται το άθροισμα των παραμέτρων της συνάρτησης
	return ss	# η συνάρτηση επιστρέφει την τιμή της ss
# υπολογισμός γινομένου
def gin(x,y):
	gg=x*y		# στη μεταβλητή gg ανατίθεται το γινόμενο των παραμέτρων της συνάρτησης
	return gg	# η συνάρτηση επιστρέφει την τιμή της gg
# υπολογισμός μέσου όρου
def mo(x,y):
	mm=(x+y)/2	# στη μεταβλητή mm ανατίθεται ο μέσος όρος των παραμέτρων της συνάρτησης
	return mm	# η συνάρτηση επιστρέφει την τιμή της mm
# εμφάνιση αποτελεσμάτων
def display(a,b):
	print('Αθροισμα =',add(a,b))
	print('Γινόμενο =',gin(a,b))
	print('Μέσος όρος =',mo(a,b))
# κεντρική συνάρτηση
def main()
	print('Υπολογισμός Αθροίσματος, Γινομένου και Μέσου όρου')
        print('-------------------------------------------------')
	a=int(input('Δώσε έναν αριθμό:'))
	b=int(input('Δώσε και άλλον αριθμό:'))
	display(a,b)	# καλεί τη συνάρτηση display() με ορίσματα τους δύο αριθμούς
# Κυρίως πρόγραμμα
main()                  # καλεί τη «κεντρική» συνάρτηση main()
