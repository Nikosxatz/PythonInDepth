def numbers(ar):
    n=1
    while True:
        yield n
        n=n+1
        if n>ar: n=1
		
# Κυρίως πρόγραμμα
for i in numbers(20):
    print(i)

