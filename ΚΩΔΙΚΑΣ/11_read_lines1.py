f=open('file3a.txt','r',encoding='utf-8')
grammes=0
pl=0
while True:
    line=f.readline()
    if line=='':
        break
 
    else:
        pl=pl+1
        mikos=len(line)
        if line.endswith('\n'):
            mikos=mikos-1
        print('Γραμμή=',pl,' Μήκος=',mikos)
f.close()

