arxeio_eikonas=input('Αρχείο εικόνας:') # Δοκιμάστε το με το αρχείο f.bmp
fp1=open(arxeio_eikonas,'rb+')

fp1.seek(2)
size_bytes=fp1.read(4)
size=int.from_bytes(size_bytes,'little')
print('Μεγεθος:',size)

fp1.seek(10)
offset_bytes=fp1.read(4)
offset=int.from_bytes(offset_bytes,'little')
print('Απόσταση δεδομένων pixel (offset):',offset)

fp1.seek(18)
platos_bytes=fp1.read(4)
ypsos_bytes=fp1.read(4)
platos=int.from_bytes(platos_bytes,'little')
print('Πλάτος:',platos)
ypsos=int.from_bytes(ypsos_bytes,'little')
print('Υψος:',ypsos)
bytes_per_raw=3*platos
if bytes_per_raw%4==0:
    padding=0
else:
    padding=4-bytes_per_raw%4
print('Byte πλήρωσης:',padding)
if padding==0:
    print('Συγνώμη αλλά το αρχείο εικόνας δεν διαθέτει byte πλήρωσης\n')
    print('Δοκίμασε εικόνα bmp 999x999 pixels\n')
    sys.exit()

fp1.seek(28)
bits_bytes=fp1.read(2)
bits=int.from_bytes(bits_bytes,'little')
print('Bits ανά pixel:',bits)
if bits!=24:
    print('Συγνώμη αλλα το αρχείο δεν είναι RGB 24bits')
    sys.exit()

print('--> Στο αρχείο εικόνας μπορούμε να κρύψουμε μέχρι', ypsos*padding,'χαρακτήρες')
count=0
arxeio_keimenoy=input('\nΔώσε το αρχείο κειμένου:') # Δοκιμάστε το με το αρχείο tocode.txt
fp2=open(arxeio_keimenoy,'r',encoding='iso-8859-7')
print('\n'+40*'=')
for g in range(ypsos):
    padding_pos=offset+platos*3*(g+1)+padding*g
    fp1.seek(padding_pos)
    for i in range(1,padding+1):
        b=fp2.read(1)
        if b:
            set_byte=bytes(b,'greek')
            fp1.write(set_byte)
            print(b,end='')
            count=count+1
        else:
            set_byte=bytes(1)
            fp1.write(set_byte)
fp1.close()
fp2.close()
print('\n'+40*'=')
print('Στην εικόνα κρύφτηκαν',count,'χαρακτήρες !!!')          
           

