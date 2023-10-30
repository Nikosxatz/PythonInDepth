b=bytearray(2)
print(len(b))
print(b)
print(b[0])
bb=bytearray(b'\x01\xffA')
print(len(bb))
b1=bytearray(b'aegean')
print(b1[0])
b1[0]=65
print(b1)
b2=bytearray('Python is eazy','utf-8')
for i in range(4,9):
    b2[i]=45
print(b2)


         
