ar=int(input('Δώσε τιμή pixel > '))
rgb=bytearray(int.to_bytes(ar,3,'big'))
print('Κόκκινο :',rgb[0])
print('Πράσινο :',rgb[1])
print('Μπλε :',rgb[2])
r=int(input('Δώσε τιμή για Κόκκινο 0~255 > '))
g=int(input('Δώσε τιμή για Πράσινο 0~255 > '))
b=int(input('Δώσε τιμή για Μπλε 0~255 > '))
rgb=bytearray(3)
rgb[0]=r
rgb[1]=g
rgb[2]=b
timi=int.from_bytes(rgb,'big')
print('Τιμή pixel > ',timi)  

