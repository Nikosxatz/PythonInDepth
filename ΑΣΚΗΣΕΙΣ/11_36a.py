import sys
fin=sys.stdin
fout=sys.stdout
Lst=[]
while True:
    onoma=fin.readline()
    if onoma=='\n':
        break
    Lst.append(onoma)
Lst.sort()
fout.writelines(Lst)