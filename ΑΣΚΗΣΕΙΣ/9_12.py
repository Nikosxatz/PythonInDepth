onomata=[]
for i in range(10):
    o=input('Δώσε όνομα : ')
    onomata.append(o)
proto=onomata[0]
kapoios_koinos=False
for i in range(len(proto)):
    xar=proto[i]
    if xar in proto[:i]:
        continue
    ola=True
    for rest in onomata[1:]:
        if xar not in rest:
            ola=False
    if ola:
        print(xar)
        kapoios_koinos=True
if not kapoios_koinos:
    print('Δεν υπάρχουν κοινοί χαρακτήρες')

    



