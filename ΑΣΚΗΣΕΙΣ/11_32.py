with open('xores_bin','rb') as fin:
    while True:
        pos=int(input('Δώσε αριθμό εγγραφής > '))
        if pos==0:
            break
        fin.seek(34*(pos-1))
        xora=fin.read(30).decode('ANSI')
        plithismos=int.from_bytes(fin.read(4),'little')
        print('Χώρα:',xora.strip(),'  Πληθυσμός:',plithismos)
