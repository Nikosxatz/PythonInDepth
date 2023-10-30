fout=open('stoixeia1.txt','w',encoding='utf-8')
with open('foit.txt','r',encoding='utf-8') as finp:
    while True:
        onoma=finp.read(30)
        kodikos=finp.read(7)
        finp.read(1)
        if onoma=='':
            break           
        print('Ονομα   : ',onoma)
        print('Κωδικός : ',kodikos)
        varos=float(input('Δώσε το βάρος του φοιτητή : '))
        if varos==0:
            break
        ypsos=float(input('Δώσε το ύψος του φοιτητή : '))
        etos=int(input('Δώσε το έτος γέννησης του φοιτητή : '))
        str_varos=str(varos).rjust(6)
        str_ypsos=str(ypsos).rjust(6)
        str_etos=str(etos).rjust(4)
        fout.write(onoma.rjust(30))
        fout.write(kodikos.rjust(7))
        fout.write(str_varos)
        fout.write(str_ypsos)
        fout.write(str_etos)
        print(40*'=')
fout.close()
