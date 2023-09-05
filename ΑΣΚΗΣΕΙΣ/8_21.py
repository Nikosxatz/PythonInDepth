def exo():
    yield 'Πατάτες'
    yield 'Καρπούζια'
    yield 'Καρέκλες'

# Κυρίως πρόγραμμα
for i in exo():
    print(i)
e=exo()
print(next(e,'Τα πάντα όλα'))
print(next(e,'Τα πάντα όλα'))
print(next(e,'Τα πάντα όλα'))
print(next(e,'Τα πάντα όλα'))


