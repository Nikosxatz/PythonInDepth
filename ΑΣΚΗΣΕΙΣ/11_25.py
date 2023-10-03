with open('stoixeia2.txt','r+',encoding='greek') as ff:
    xar=input('Δώσε αρχικούς χαρακτήρες > ')
    et=int(input('Δώσε τρέχον έτος > '))
    while True:
        onoma=ff.read(30)
        if onoma=='':
            break
        if onoma.startswith(xar):
            ff.read(19)
            etos=int(ff.read(4))
            ilikia=et-etos
            print(onoma,ilikia)
        else:
            ff.read(23)
