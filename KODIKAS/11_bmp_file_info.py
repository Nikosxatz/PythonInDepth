fp1=open('python_logo.bmp','rb')
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

fp1.close()
       
           

