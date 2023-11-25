ar=int(input("Δώσε έναν ακέραιο θετικό αριθμό:"))
s=str(ar)
kat=0
x=0
for i in s:
    y=int(i)
    kat=kat+y*(10**x)
    x+=1
print('Ο κατοπτρικός του {} είναι ο {}'.format(ar,kat))
    
















