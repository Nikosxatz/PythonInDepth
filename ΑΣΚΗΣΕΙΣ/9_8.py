onomata=[]

while True:
    o=input('Δώσε όνομα : ')
    if o=='':
        break
    if o in onomata:
        print('Το όνομα υπάρχει ήδη')
    else:
        onomata.append(o)
print(onomata)


    



