f=open('file3a.txt','r',encoding='utf-8')
grammes=0
pl=0
for line in f:
        pl=pl+1
        mikos=len(line)
        if line.endswith('\n'):
            mikos=mikos-1
        print('Γραμμή=',pl,' Χαρακτήρες=',mikos)
f.close()

