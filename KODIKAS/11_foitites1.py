with open('foit.txt','r',encoding='utf-8') as inp:
    while True:
        eggr=int(input('Δώσε α/α εγγραφής >'))
        if eggr==0:
            break
        inp.seek((eggr-1)*39)
        onoma=inp.read(30)
        kodikos=inp.read(7)
        if onoma=='':
            print('Δεν υπάρχει τέτοια εγγραφή!')
        else:
            print('Ονομα   : ',onoma)
            print('Κωδικός : ',kodikos)

