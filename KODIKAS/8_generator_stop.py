def test():
	yield 1
	yield 2
	yield 'Python'

g=test()
for i in range(4):
	print(next(g))

