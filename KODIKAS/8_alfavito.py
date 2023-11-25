def alfavito():
    n = 0
    ab='ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
    while True:
        if n<24:
            yield ab[n]
            n=n+1
        else:
            n=0
            yield ab[n]
                
# Κυρίως πρόγραμμα
a=alfavito()
for i in range(5):
    print(next(a))
for i in range(5):
    print(a.__next__())

