def plaisio1(y,p): # ο κλασικός τρόπος
    for pl in range(p):
        print('*',end='')
    print()
    for g in range(y-2):
        print('*',end='')
        for pl in range(p-2):
            print(' ',end='')
        print('*')
    for pl in range(p):
        print('*',end='')
    print()

def plaisio2(y,p): # ο «Πυθωνικός» τρόπος
    print('*'*p+'\n'+('*'+' '*(p-2)+'*\n')*(y-2)+'*'*p+'\n')
    
# Κυρίως πρόγραμμα
plaisio1(6,10)
print()
plaisio2(6,10)
