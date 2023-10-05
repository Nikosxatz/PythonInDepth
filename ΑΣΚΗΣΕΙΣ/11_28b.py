fin=open('in.txt','r',encoding='utf-8')
fout=open('out.txt','w')
while True:
    onoma=fin.readline()
    if onoma=='':
        break
    etos=fin.readline()
    onoma=onoma[:-1].ljust(20)
    fout.write(onoma)
    fout.write(etos[:4].rjust(4))
    fout.write('\n')
fout.close() 
fin.close()

