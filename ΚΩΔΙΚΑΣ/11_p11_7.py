tmima=input('Δώσε τμήμα του ονόματος για αναζήτηση > ')
found=False
with open('stoixeia2.txt','r',encoding='utf-8') as finp:
    while True:
        onoma=finp.read(30)
        if onoma=='':
            break
        kodikos=finp.read(7)
        varos=float(finp.read(6))
        ypsos=float(finp.read(6))
        etos=int(finp.read(4))
        if tmima in onoma:
            found=True
            print('Ονομα   : ',onoma)
            print('Κωδικός : ',kodikos)
            print('Βάρος   : ',varos)
            print('Ύψος    : ',ypsos)
            print('Έτος    : ',etos)
            print(40*'=')
if not found:
    print('Δεν βρέθηκε κανένας με αυτούς τους χαρακτήρες')
