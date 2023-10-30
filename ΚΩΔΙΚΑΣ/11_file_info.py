f=open('file3a.txt','r',encoding='utf-8')
grammes=0
asc=0
uni=0
kef=0
peza=0
pl=0
kena=0
while True:
    ch=f.read(1)
    if ch=='':
        break
    elif ch=='\n':
        grammes=grammes+1
    elif ch==' ':
        kena=kena+1
    else:
        pl=pl+1
        if ch.islower():
            peza=peza+1    
        elif ch.isupper():
            kef=kef+1
        if ch.isascii():
            asc=asc+1
        else:
            uni=uni+1
f.close()
print('Πλήθος=',pl,' Κενά=',kena,'Γραμμές=',grammes+1)
print('Κεφαλαία=',kef,' Πεζά=',peza)
print('ASCII=',asc,' UNICODE=',uni)
