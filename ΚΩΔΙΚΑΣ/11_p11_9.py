import sys

input_file=input('Δώσε όνομα αρχείου εισόδου για κωδικοποίηση  > ')
output_file=input('Δώσε όνομα αρχείου εξόδου  > ')

fin=open(input_file,'rb')
fout=open(output_file,'wb')

while True:
    b=fin.read(1)
    if b==b'':
        break
    ar=int.from_bytes(b,'little')
    ar=255^ar
    b=ar.to_bytes(1,'little')
    fout.write(b)
fin.close()
fout.close()             
           

