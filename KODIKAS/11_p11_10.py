import sys

fp1=open('p.bmp','rb')
fp1.seek(2)
size_bytes=fp1.read(4)
size=int.from_bytes(size_bytes,'little')
print('Μεγεθος:',size)

fp1.seek(10)
offset_bytes=fp1.read(4)
offset=int.from_bytes(offset_bytes,'little')
print('Offset:',offset)

fp1.seek(18)
platos_bytes=fp1.read(4)
ypsos_bytes=fp1.read(4)
platos=int.from_bytes(platos_bytes,'little')
print('Πλάτος:',platos)
ypsos=int.from_bytes(ypsos_bytes,'little')
print('Υψος:',ypsos)

bytes_per_raw=3*platos
padding=(4-bytes_per_raw%4)%4 # Υπάρχει τυπογραφικό λάθος στο βιβλίο η σωστή παράσταση είναι αυτή
print('Πλήρωση:',padding)

fp1.seek(28)
bits_bytes=fp1.read(2)
bits=int.from_bytes(bits_bytes,'little')
print('Bits ανά pixel:',bits)
if bits!=24:
    print('Συγνώμη αλλα το αρχείο δεν είναι RGB 24bits')
    sys.exit()

fp1.seek(offset)
for g in range(ypsos):
    for s in range(platos):
        rgb=fp1.read(3)
        if rgb[0]!=255 or rgb[1]!=255 or rgb[2]!=255:
            print(g,'-',s,' -> Red:',rgb[2],' Green:',rgb[1],' Blue:',rgb[0])
    fp1.seek(padding,1)
fp1.close()
print(37*'=')                 
           

