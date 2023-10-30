def test():
	yield 1
	yield 2
	yield 'Python'
	yield 'Τέλος'
	
# Κυρίως πρόγραμμα
for i in test():
	print(i)

