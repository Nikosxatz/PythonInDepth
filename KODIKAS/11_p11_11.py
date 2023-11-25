import sys
import random
input_file=input('Δώσε όνομα αρχείου εισόδου χωρίς την προέκταση .bmp  > ')
input_file=input_file+'.bmp'
output_file=input('Δώσε όνομα αρχείου εξόδου χωρίς την προέκταση .bmp  > ')
output_file=output_file+'.bmp'
code=int(input('Δώσε κωδικό κωδικοποίησης/αποκωδικοποίησης  > '))
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
padding=(4-bytes_per_raw%4)%4  # Υπάρχει τυπογραφικό λάθος στο βιβλίο η σωστή παράσταση είναι αυτή

fin.seek(28)
bits_bytes=fin.read(2)
bits=int.from_bytes(bits_bytes,'little')
print('Bits ανά pixel:',bits)
if bits!=24:
    print('Συγνώμη αλλα το αρχείο δεν είναι RGB 24bits')
    sys.exit()

fin.seek(0)
header=fin.read(offset)
fout.write(header)
fin.seek(offset)
random.seed(code)
for g in range(ypsos):
    for s in range(platos):
        rgb=bytearray(fin.read(3))
        rgb[0]=rgb[0]^random.randint(0,255)
        rgb[1]=rgb[1]^random.randint(0,255)
        rgb[2]=rgb[2]^random.randint(0,255)
        fout.write(rgb)
    fin.seek(padding,1)
    if padding>0:
        pad=bytes(padding)
        fout.write(pad)
fin.close()
fout.close()
print('Η νέα εικόνα βρίσκεται στο αρχείο ',output_file)                 
           

