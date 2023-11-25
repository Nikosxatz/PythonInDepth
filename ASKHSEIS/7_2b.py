# Σωστή έκδοση της άσκησης 7.2
def mo(a,b,c):
	mm=(a+b+c)/3
	return mm
def apotelesma(m):
	if m>=8.5:
		print('Μπράβο άριστα!')
	elif m>=6.5:
		print('Αρκετά καλά')
	elif m>=5:
		print('Πέρασες')
	else:
		print('Δυστυχώς κόπηκες')
# Κυρίως πρόγραμμα
mesos=mo(8,7,10)
apotelesma(mesos)


