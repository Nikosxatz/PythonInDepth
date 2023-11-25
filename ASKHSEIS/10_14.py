b=bytes(3)
print(len(b))
print(b)
print(b[1])
bb=bytes(b'\x01\xff')
print(len(bb))
print(bb[0],bb[1])
b1=bytes(b'Python!')
print(len(b1))
for i in b1:
    print(i)
b2=bytes('Η Python είναι εύκολη','utf-8')
print(len(b2))
print(b2[3:9])
b3=bytes(range(200,204))
print(len(b3))
print(b3)

         
