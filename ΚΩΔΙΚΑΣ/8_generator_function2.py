def test():
	yield 1
	yield 2
	yield 'Python'
	yield 'Τέλος'
	
# Κυρίως πρόγραμμα
g=test()
print(next(g))
print(next(g))
print(next(g))

