with open('stoixeia2.txt','r',encoding='greek') as finp:
    while True:
        pos=int(input('Δώσε αριθμό εγγραφής > '))
        if pos==0:
            break
        finp.seek(53*(pos-1))
        onoma=finp.read(30)
        if onoma=='':
            print('Δεν υπάρχει τέτοια εγγραφή!')
            continue
        kodikos=finp.read(7)
        varos=float(finp.read(6))
        ypsos=float(finp.read(6))
        etos=int(finp.read(4))
        print('Όνομα :',onoma)
        print('Κωδικός :',kodikos)
        print('Βάρος :',varos)
        print('Ύψος :',ypsos)
        print('Έτος :',etos)
