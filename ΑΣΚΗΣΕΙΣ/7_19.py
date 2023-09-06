def test(m,v):
    if m>=v:
        return True
    else:
        return False

def apot(o,b1,b2,vasi):
    mo=(b1+b2)/2
    if test(mo,vasi):
        print(o,'πέρασες με',mo)
    else:
        print(o,'κόπηκες')
    
apot('Μιχαήλ',7,8,5)
apot('Μιχαήλ',b2=7,vasi=8,b1=5)
apot(vasi=3,b2=4,b1=5,o='Χρυσάνθη',) 
