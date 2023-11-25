def test():
	yield 1
	yield 2
	yield 'Python'

g=test()
print(next(g))
print(next(g))
g.close()
print(next(g))


