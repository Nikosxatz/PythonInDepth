def mesos(arista,basi,*bath):
    s=0
    ar=0
    kop=0
    for i in bath:
        s=s+i
        if i>=arista:
            ar+=1
        elif i<basi:
            kop+=1
    if len(bath)==0:
        return None
    else:
        print('Αριστούχοι:',ar)
        print('Κόπηκαν:',kop)
        return s/len(bath)

# Κυρίως πρόγραμμα
print('Μέσος όρος=',mesos(8,5,3,4,7,8,9))			
print('Μέσος όρος=',mesos(9,4,3,4,7,8,9))
print('Μέσος όρος=',mesos(8.5,5))








