def nisia():
    n=('Ψαρά','Αρκοί','Μαράθι','Ηρακλειά','Ανάφη')
    for i in n:
        yield i
        
# Κυρίως πρόγραμμα
n=nisia()
for i in n:
    print(i)
print('--------')
n=nisia()
print(next(n))
print(next(n))
print(next(n))
						


