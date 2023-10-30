with open('file3a.txt','rb+') as f:
    b=f.readline()
    print(b)
    f.seek(-12,2)
    lex='δύσκολη'
    f.write(lex.encode('utf-8'))
    f.seek(2,2)
    f.write(b';;;')
             
