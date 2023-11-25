with open('stoixeia2.txt','r',encoding='cp1253') as finp:
    found=False
    while True:
        onoma=finp.read(30)
        if onoma=='':
            break
        kodikos=finp.read(7)
        varos=float(finp.read(6))
        ypsos=float(finp.read(6))
        etos=int(finp.read(4))
        dms=varos/ypsos**2
        if dms>=30:
            print(onoma)
            found=True

if not found:
    print('Δεν βρέθηκε κανένας παχύσαρκος')
