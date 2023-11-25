import sys

input_file=input('Δώσε όνομα αρχείου εισόδου χωρίς την προέκταση .bmp  > ')
input_file=input_file+'.bmp'
output_file=input('Δώσε όνομα αρχείου εξόδου χωρίς την προέκταση .bmp  > ')
output_file=output_file+'.bmp'
print('Δώσε χρώμα RGB πλαισίου')
plaisio_red=int(input('Τιμή κόκκινου (0~255) -> '))
plaisio_green=int(input('Τιμή πράσινου (0~255) -> '))
plaisio_blue=int(input('Τιμή μπλε (0~255) -> '))

print('Δώσε πάχος πλαισίου σε pixel')
paxos=int(input('Πάχος πλαισίου -> '))

fin=open(input_file,'rb')
fout=open(output_file,'wb')

fin.seek(10)
offset_bytes=fin.read(4)
offset=int.from_bytes(offset_bytes,'little')

fin.seek(18)
platos_bytes=fin.read(4)
ypsos_bytes=fin.read(4)
platos=int.from_bytes(platos_bytes,'little')
ypsos=int.from_bytes(ypsos_bytes,'little')

bytes_per_raw=3*platos
padding=(4-bytes_per_raw%4)%4 # Υπάρχει τυπογραφικό λάθος στο βιβλίο η σωστή παράσταση είναι αυτή
print('Byte πλήρωσης:',padding)

fin.seek(28)
bits_bytes=fin.read(2)
bits=int.from_bytes(bits_bytes,'little')
print('Bits per pixel:',bits)
if bits!=24:
    print('Συγνώμη αλλα το αρχείο δεν είναι RGB 24bits')
    sys.exit()

fin.seek(0)
header=fin.read(offset)
fout.write(header)
fin.seek(offset)

for g in range(ypsos):
    for s in range(platos):
        rgb=bytearray(fin.read(3))
        if g<paxos or s<paxos or g>=ypsos-paxos or s>=platos-paxos:
            rgb[2]=plaisio_red
            rgb[1]=plaisio_green
            rgb[0]=plaisio_blue
        fout.write(rgb)
    fin.seek(padding,1)
    if padding>0:
        pad=bytes(padding)
        fout.write(pad)
fin.close()
fout.close()             
           

