fin=open('xores.txt','r',encoding='utf-8')
Lst=[]
for line in fin:
    fields=line.split(',')
    fields[1]=int(fields[1])
    Lst.append(fields)
fin.close()
Lst.sort()
with open('xores_bin','wb') as fout:
    for x in Lst:
        onoma=x[0].encode('ANSI')
        onoma=onoma.ljust(30)[:30]
        plith=int.to_bytes(x[1],4,'little')
        fout.write(onoma)
        fout.write(plith)
