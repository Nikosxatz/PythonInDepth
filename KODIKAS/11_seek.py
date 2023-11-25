with open('file3a.txt','ab+') as f:
    f.seek(8)
    print('Θέση:',f.tell())
    b=f.read(1)
    print(int.from_bytes(b))
    print('Θέση:',f.tell())
    f.seek(5,1)
    b=f.read(1)
    print(int.from_bytes(b))
    f.seek(-9,2)
    print('Θέση:',f.tell())
    b=f.read(1)
    print(int.from_bytes(b))
    f.seek(3,2)
    print('Θέση:',f.tell())
    
    
             
