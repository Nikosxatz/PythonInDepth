with open('foit.txt','r+') as f:
    while True:
        eggr=int(input('Δώσε α/α εγγραφής >'))
        if eggr==0:
            break
        f.seek((eggr-1)*39)
        onoma=f.read(30)
        kodikos=f.read(7)
        if onoma=='':
            print('Δεν υπάρχει τέτοια εγγραφή!')
        else:
            print('Ονομα   : ',onoma)
            print('Κωδικός : ',kodikos)
        f.seek((eggr-1)*39)
        onoma=input('Δώσε νέο όνομα :')
        kodikos=input('Δώσε νέο κωδικό :')       
        onoma=onoma[:30]
        kodikos=kodikos[:7]
        onoma=onoma.ljust(30)
        kodikos=kodikos.ljust(7)
        f.write(onoma)
        f.write(kodikos)
