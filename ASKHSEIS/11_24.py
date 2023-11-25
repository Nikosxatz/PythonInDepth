with open('stoixeia2.txt','r+',encoding='greek') as ff:
    while True:
        pos=int(input('Δώσε αριθμό εγγραφής > '))
        if pos==0:
            break
        ff.seek(53*(pos-1))
        onoma=ff.read(30)
        if onoma=='':
            print('Δεν υπάρχει τέτοια εγγραφή!')
            continue
        kodikos=ff.read(7)
        varos=float(ff.read(6))
        ypsos=float(ff.read(6))
        etos=int(ff.read(4))
        print('Όνομα :',onoma)
        print('Κωδικός :',kodikos)
        print('Βάρος :',varos)
        print('Ύψος :',ypsos)
        print('Έτος :',etos)
        ans=input('Θέλετε να αλλάξετε τα στοιχεία βάρους & ύψους Ν/Ο ;')
        if ans in 'ΝνNn':
            varos=float(input('Δώσε το βάρος του φοιτητή : '))
            ypsos=float(input('Δώσε το ύψος του φοιτητή : '))
            str_varos=str(varos).rjust(6)
            str_ypsos=str(ypsos).rjust(6)
            ff.seek(53*(pos-1)+37)
            ff.write(str_varos)
            ff.write(str_ypsos)

