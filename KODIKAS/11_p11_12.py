import sys

input_file=input('Δώσε όνομα αρχείου χωρίς την προέκταση .bmp  > ')
input_file=input_file+'.bmp'

print('Δώσε χρώμα RGB των Pixel για αντικατάσταση')
old_red=int(input('Τιμή κόκκινου (0~255) -> '))
old_green=int(input('Τιμή πράσινου (0~255) -> '))
old_blue=int(input('Τιμή μπλε (0~255) -> '))

print('Δώσε νέο χρώμα RGB')
new_red=int(input('Τιμή κόκκινου (0~255) -> '))
new_green=int(input('Τιμή πράσινου (0~255) -> '))
new_blue=int(input('Τιμή μπλε (0~255) -> '))

fin=open(input_file,'rb+')


fin.seek(10)
offset_bytes=fin.read(4)
offset=int.from_bytes(offset_bytes,'little')

fin.seek(18)
platos_bytes=fin.read(4)
ypsos_bytes=fin.read(4)
platos=int.from_bytes(platos_bytes,'little')
ypsos=int.from_bytes(ypsos_bytes,'little')

bytes_per_raw=3*platos
padding=(4-bytes_per_raw%4)%4    # Υπάρχει τυπογραφικό λάθος στο βιβλίο η σωστή παράσταση είναι αυτή

fin.seek(28)
bits_bytes=fin.read(2)
bits=int.from_bytes(bits_bytes,'little')

if bits!=24:
    print("Συγνώμη αλλα το αρχείο δεν είναι RGB 24bits")
    sys.exit()

fin.seek(offset)

for g in range(ypsos):
    for s in range(platos):
        rgb=bytearray(fin.read(3))
        if rgb[2]==old_red and rgb[1]==old_green and rgb[0]==old_blue:         
            rgb[2]=new_red
            rgb[1]=new_green
            rgb[0]=new_blue
        fin.seek(-3,1)
        fin.write(rgb)
    fin.seek(padding,1)
fin.close()
          
           

