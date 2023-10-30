with open('file3a.txt','rb') as f:
    b=f.read()
    for i in b:
        print(i,end='-')
    f.seek(11)
    lex=f.read(10)
    s=lex.decode('utf-8')
    print()
    print(s)
             
